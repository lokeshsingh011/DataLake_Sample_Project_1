import os
import pandas as pd
import shutil
from io import StringIO

def read_data(file_path):
    """Read data from a CSV or JSON file, handling JSON files with CSV content."""
    print(f"Reading data from {file_path}")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File does not exist: {file_path}")
    
    if os.path.getsize(file_path) == 0:
        raise ValueError(f"File is empty: {file_path}")
    
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
            if df.empty:
                raise ValueError(f"File contains no data (empty DataFrame): {file_path}")
            return df
        elif file_path.endswith(".json"):
            # Read the file content to check if it's CSV data
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            # Check if content resembles CSV (e.g., contains commas and headers)
            if content and ',' in content and not content.startswith('{') and not content.startswith('['):
                # Parse as CSV using StringIO
                df = pd.read_csv(StringIO(content))
                if df.empty:
                    raise ValueError(f"File contains no data (empty DataFrame): {file_path}")
                return df
            else:
                # Try parsing as JSON
                df = pd.read_json(file_path)
                if df.empty:
                    raise ValueError(f"File contains no data (empty DataFrame): {file_path}")
                return df
        else:
            raise ValueError("Unsupported file format. Please use .csv or .json files.")
    except pd.errors.EmptyDataError:
        raise ValueError(f"File is empty or corrupted: {file_path}")
    except pd.errors.ParserError:
        raise ValueError(f"File is not a valid CSV or JSON: {file_path}")
    except Exception as e:
        raise ValueError(f"Error reading file {file_path}: {str(e)}")

def ingest_data(src_path, dest_path):
    """Copy a file or directory to the destination path."""
    os.makedirs(dest_path, exist_ok=True)
    
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Source path does not exist: {src_path}")
    
    if os.path.isfile(src_path):
        dest_file = os.path.join(dest_path, os.path.basename(src_path))
        shutil.copy(src_path, dest_file)
        print(f"Copied file: {src_path} to {dest_file}")
    elif os.path.isdir(src_path):
        dest_dir = os.path.join(dest_path, os.path.basename(src_path))
        shutil.copytree(src_path, dest_dir, dirs_exist_ok=True)
        print(f"Copied directory: {src_path} to {dest_dir}")
    else:
        raise ValueError(f"Source path is neither a file nor a directory: {src_path}")

def perform_data_operations(data, layer):
    """Perform data operations based on the specified layer."""
    print(f"Performing data operations on {layer} layer...")
    
    result = data.copy()  # Avoid in-place modifications
    
    if layer == 'refined':
        result = result.drop(columns=['Cabin', 'Ticket'], errors='ignore')
        result = result.dropna(how='all')
        result['Processed'] = True

    elif layer == 'curated':
        if 'Sex' in result.columns:
            result['Sex'] = result['Sex'].str.lower()
        if 'Age' in result.columns:
            result['Age'] = result['Age'].fillna(result['Age'].median())
        if 'Embarked' in result.columns:
            result['Embarked'] = result['Embarked'].map({'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'})

    elif layer == 'enriched':
        if 'Age' in result.columns:
            result['AgeGroup'] = pd.cut(result['Age'], bins=[0, 12, 60, 120], labels=['Child', 'Adult', 'Senior'])
        if 'SibSp' in result.columns and 'Parch' in result.columns:
            result['FamilySize'] = result['SibSp'] + result['Parch']
            result['IsAlone'] = (result['FamilySize'] == 0).astype(int)

    elif layer == 'transformed':
        if 'Pclass' in result.columns and 'Embarked' in result.columns and 'Survived' in result.columns:
            transformed = result.groupby(['Pclass', 'Embarked'])['Survived'].mean().reset_index()
            transformed.rename(columns={'Survived': 'SurvivalRate'}, inplace=True)
            if 'Fare' in result.columns:
                fare_by_port = result.groupby('Embarked')['Fare'].mean().reset_index()
                transformed = pd.merge(transformed, fare_by_port, how='left', on='Embarked')
            return transformed
        else:
            print(f"Warning: Skipping transformed layer due to missing columns")
            return result

    return result

def main():
    try:
        # Define paths
        project_path = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(project_path, 'data')
        data_lake_path = os.path.join(project_path, 'data_lake')

        # Define layers
        raw_path = os.path.join(data_lake_path, 'raw')
        refined_path = os.path.join(data_lake_path, 'refined')
        curated_path = os.path.join(data_lake_path, 'curated')
        enriched_path = os.path.join(data_lake_path, 'enriched')
        transformed_path = os.path.join(data_lake_path, 'transformed')

        # Create directories for each layer
        for layer_path in [raw_path, refined_path, curated_path, enriched_path, transformed_path]:
            os.makedirs(layer_path, exist_ok=True)
        
        # Process all CSV and JSON files in data directory
        for file_name in os.listdir(data_path):
            if file_name.endswith(('.csv', '.json')):
                source_file = os.path.join(data_path, file_name)
                ingest_data(source_file, raw_path)
                raw_file = os.path.join(raw_path, file_name)

                data = read_data(raw_file)

                refined_data = perform_data_operations(data, 'refined')
                refined_output = os.path.join(refined_path, file_name)
                refined_data.to_csv(refined_output, index=False)
                print(f"Saved refined data to {refined_output}")

                curated_data = perform_data_operations(refined_data, 'curated')
                curated_output = os.path.join(curated_path, file_name)
                curated_data.to_csv(curated_output, index=False)
                print(f"Saved curated data to {curated_output}")

                enriched_data = perform_data_operations(curated_data, 'enriched')
                enriched_output = os.path.join(enriched_path, file_name)
                enriched_data.to_csv(enriched_output, index=False)
                print(f"Saved enriched data to {enriched_output}")

                transformed_data = perform_data_operations(enriched_data, 'transformed')
                transformed_output = os.path.join(transformed_path, file_name)
                transformed_data.to_csv(transformed_output, index=False)
                print(f"Saved transformed data to {transformed_output}")

        print("✅ Data processing pipeline complete.")

    except Exception as e:
        print(f"Error in pipeline: {str(e)}")
        raise

if __name__ == "__main__":
    main()
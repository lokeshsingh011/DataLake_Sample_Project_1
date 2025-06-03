# DataLake_Sample_Project_1


🛠️ Data Lake Project - Titanic Dataset

This project demonstrates the implementation of a multi-layered data lake architecture using Python, applied to a modified Titanic dataset. It includes data ingestion, transformation, and analytics, showcasing the core principles of data engineering.

📁 Project Structure
--------------------
Data-Lake-Project/
├── data/
│   ├── sample.json           - Sample JSON file (may contain CSV data)
│   └── sample.csv            - Sample CSV file
├── data_lake/
│   ├── raw/                  - Raw layer: Initial ingested data
│   ├── refined/              - Refined layer: Cleaned data
│   ├── curated/              - Curated layer: Standardized data
│   ├── enriched/             - Enriched layer: Enhanced data with new features
│   └── transformed/          - Transformed layer: Aggregated and summarized data
├── visualizations/           - Directory for generated charts (currently empty)
├── main.py                   - Main pipeline script for data processing
├── analytics_visualization.py - Script for analytics and visualization (to be implemented)
└── README.md                 - Project documentation



You can view the structured directory here 
![{6B8D2F44-4438-47C6-BDD7-D735A234A5FE}](https://github.com/user-attachments/assets/206be39c-427b-4593-bf77-d910fe45f2c8)


🌊 Data Lake Layers
--------------------
Each layer of the data lake stores progressively processed versions of the dataset:

- Raw: Original unprocessed data.
- Refined: Cleaned data with basic formatting.
- Curated: Structured data with selected features.
- Enriched: Additional derived metrics or columns.
- Transformed: Final output ready for analytics and reporting.

🔄 Data Pipeline
--------------------
The pipeline performs the following tasks:
1. Loads raw JSON data.
2. Processes and saves each stage to its corresponding layer.
3. Converts final output to CSV format for analysis.

📊 Analytics and Visualization
--------------------
The analytics_visualization.py script performs insights and visualization on the transformed data.

Visualizations Include:
- Survival Rate by Passenger Class
- Average Fare by Class
- Survival Rate by Embarkation Port
- Correlation Heatmap between Fare and Survival Rate

All charts are saved in:  
data_lake/visualizations/

📦 Requirements
--------------------
Install the required Python packages:

pip install pandas matplotlib seaborn

▶️ How to Run
--------------------
1. Run the Data Pipeline:
   python main.py

2. Generate Analytics and Charts:
   python analytics_visualization.py

🧠 Insights
--------------------
The transformed dataset shows survival patterns across different passenger classes and ports of embarkation, with meaningful correlations between fare and survival rates. The project mirrors real-world ETL + analytics pipelines used in data engineering.

🏁 Final Notes
--------------------
This project is part of my learning journey to become a Data Engineer.  
Feel free to fork, adapt, or contribute ideas!

🙋‍♂️ Author
--------------------
Lokesh Kumar
LinkedIn: https://www.linkedin.com/in/lokesh-kumar-ab41a819a/

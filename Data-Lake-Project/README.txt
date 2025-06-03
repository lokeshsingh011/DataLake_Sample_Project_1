
🛠️ Data Lake Project - Titanic Dataset

This project demonstrates the implementation of a multi-layered data lake architecture using Python, applied to a modified Titanic dataset. It includes data ingestion, transformation, and analytics, showcasing the core principles of data engineering.

📁 Project Structure
--------------------
Data-Lake-Project/
│
├── data/                        # Source data
│   └── sample.json
│
├── data_lake/                  # Data Lake structure
│   ├── raw/
│   ├── refined/
│   ├── curated/
│   ├── enriched/
│   ├── transformed/
│   │   └── sample.csv
│   └── visualizations/         # Generated charts
│
├── main.py                 # Main data pipeline script
├── analytics_visualization.py # Analytics and visualization script
└── README.txt                  # Project documentation

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

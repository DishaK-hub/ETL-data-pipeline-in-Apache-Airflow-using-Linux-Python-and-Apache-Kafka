**National Highway Traffic ETL Pipeline**

*Overview* 

This project is an ETL (Extract, Transform, Load) pipeline built to analyze and consolidate road traffic data from various toll plazas across national highways. Each highway is operated by a different toll operator, each with its own IT setup and file formats. The main objective of this project is to collect data from multiple sources, standardize it, and consolidate it into a single, analysis-ready dataset to help de-congest traffic and optimize highway operations.
The pipeline is implemented using Apache Airflow and Python, leveraging both PythonOperators and BashOperators to manage the ETL workflow.

*Features*
1. Data Extraction: Handles multiple file formats from different toll operators- CSV (vehicle-data.csv), TSV (tollplaza-data.tsv), Fixed-width text files (payment-data.txt)
2. Data Transformation: Standardizes column formats (e.g., converting vehicle types to uppercase), ensures consistent and clean data across all sources
3. Data Consolidation: Combines all extracted and transformed data into a single CSV file ready for downstream analytics.

*Automated Workflow*

Uses Apache Airflow DAG to automate the ETL pipeline, daily scheduling of the pipeline for regular updates, supports retry and error notifications

*ETL Pipeline Steps*
1. Download Data: Fetches the dataset from a public S3 bucket.
2. Extract Data: Extracts CSV, TSV, and fixed-width files into standardized CSV formats.
3. Consolidate Data: Combines the extracted files into a single dataset.
4. Transform Data: Cleans and standardizes the dataset (e.g., uppercase vehicle types).
5. Load Data: Saves the final consolidated and transformed dataset to the staging directory.

*Technologies Used*

Python 3 – Data processing and scripting

Apache Airflow – Workflow orchestration

Bash – File extraction and manipulation

CSV / TSV handling – Python csv module

Requests – For downloading datasets

Tarfile – Extracting compressed files

*Outcome*

The pipeline produces a single CSV file transformed_data.csv with the following structure:
| Rowid | Timestamp | Anonymized Vehicle Number | Vehicle Type | Number of Axles | Tollplaza ID | Tollplaza Code | Type of Payment Code | Vehicle Code |
This consolidated dataset can be used for traffic analysis, reporting, and planning highway decongestion strategies.

#National Highway Traffic ETL Pipeline
Overview

This project is an ETL (Extract, Transform, Load) pipeline built to analyze and consolidate road traffic data from various toll plazas across national highways. Each highway is operated by a different toll operator, each with its own IT setup and file formats. The main objective of this project is to collect data from multiple sources, standardize it, and consolidate it into a single, analysis-ready dataset to help de-congest traffic and optimize highway operations.

The pipeline is implemented using Apache Airflow and Python, leveraging both PythonOperators and BashOperators to manage the ETL workflow.

Features

Data Extraction
Handles multiple file formats from different toll operators:

CSV (vehicle-data.csv)

TSV (tollplaza-data.tsv)

Fixed-width text files (payment-data.txt)

Data Transformation

Standardizes column formats (e.g., converting vehicle types to uppercase)

Ensures consistent and clean data across all sources

Data Consolidation
Combines all extracted and transformed data into a single CSV file ready for downstream analytics.

Automated Workflow

Uses Apache Airflow DAG to automate the ETL pipeline

Daily scheduling of the pipeline for regular updates

Supports retry and error notifications

Project Structure
project/
│
├── dags/
│   ├── python_etl/
│   │   ├── etl_toll_data.py        # PythonOperator ETL DAG
│   │   └── staging/                # Staging directory for intermediate files
│   └── bash_etl/
│       └── etl_toll_data_bash.py   # BashOperator ETL DAG
│
├── README.md
└── requirements.txt

ETL Pipeline Steps

Download Data

Fetches the dataset from a public S3 bucket.

Extract Data

Extracts CSV, TSV, and fixed-width files into standardized CSV formats.

Consolidate Data

Combines the extracted files into a single dataset.

Transform Data

Cleans and standardizes the dataset (e.g., uppercase vehicle types).

Load Data

Saves the final consolidated and transformed dataset to the staging directory.

Technologies Used

Python 3 – Data processing and scripting

Apache Airflow – Workflow orchestration

Bash – File extraction and manipulation

CSV / TSV handling – Python csv module

Requests – For downloading datasets

Tarfile – Extracting compressed files

How to Run

Clone the repository:

git clone <repo-url>
cd <repo-directory>


Ensure Apache Airflow is installed and running.

Place the DAG file(s) in the Airflow dags/ directory.

Trigger the DAG via the Airflow UI or CLI. The pipeline will automatically:

Download the dataset

Extract files

Consolidate and transform the data

Store the final CSV in the staging/ folder

Outcome

The pipeline produces a single CSV file transformed_data.csv with the following structure:

| Rowid | Timestamp | Anonymized Vehicle Number | Vehicle Type | Number of Axles | Tollplaza ID | Tollplaza Code | Type of Payment Code | Vehicle Code |

This consolidated dataset can be used for traffic analysis, reporting, and planning highway decongestion strategies.

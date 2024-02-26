# Week1: Building a Data Modeling with Postgres (SQL)

## Description

To perform ETL (Extract, Transform, Load) from multiple JSON files and store the data in a PostgreSQL database running on Docker, along with creating four tables (events, repo, payload, actors) to store the data, you can follow these steps:

## Prosesc
1. Extract:
- Read data from multiple JSON files.
- Extract relevant fields from each JSON object.

2. Transform:
- Cleanse and transform the extracted data if necessary.
- Ensure data consistency and integrity.
- Map the JSON fields to the corresponding columns in the database tables.

3. Load:
- Connect to the PostgreSQL database running on Docker.
- Create the necessary tables (events, repo, payload, actors) if they don't exist.
- Insert the transformed data into the respective tables.
  
## Library Python

- Python 3.x
- PostgreSQL
- psycopg2 library (`pip install psycopg2`)

## Installation

1. Clone this repository to your local machine:

```bash
$ git clone https://github.com/your_username/github-event-data-processing.git

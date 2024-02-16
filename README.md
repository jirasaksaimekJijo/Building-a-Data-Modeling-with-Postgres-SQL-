# Week1: Building a Data Modeling with Postgres (SQL)

## Description

This Python script is designed to process event data from GitHub contained in JSON files and insert it into corresponding tables in a PostgreSQL database. The script parses each JSON file, extracts relevant information such as event type, actor details, repository details, and payload information, and inserts this data into the database tables.

## Requirements

- Python 3.x
- PostgreSQL
- psycopg2 library (`pip install psycopg2`)

## Installation

1. Clone this repository to your local machine:

```bash
$ git clone https://github.com/your_username/github-event-data-processing.git

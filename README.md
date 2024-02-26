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
- glob
- json
- os
- psycopg2 
  
`If Library doesn't give`
```bash
$ pip install ..... (Library Name)
```

## Working steps of this project
### Step 1: Running PostgreSQL on Docker
Running PostgreSQL on Docker allows you to deploy and manage a PostgreSQL database system within a Docker container. Docker is a platform that enables developers to package applications and their dependencies into lightweight containers, which can then be easily deployed across different environments.

1. Run the environment so that the tools can be used to perform tasks.
But because we have a file .yml

run in command line
```bash
docker compose up
```

### Step 2: Create a table for storing data on Postgres
The tables that you can create to store the data are divided into 4 tables as you mentioned:

1. Events Table:
Used to store data related to events that occur, such as ID, type, actor ID, and a foreign key constraint on actor_id.
```bash
    CREATE TABLE IF NOT EXISTS events (
        id text PRIMARY KEY,
        type text,
        actor_id int,
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)
    )
```

2. Repo Table:
Used to store data related to repositories associated with ID, name, URL, actor ID, and a foreign key constraint on actor_id.

```bash
    CREATE TABLE IF NOT EXISTS repo (
        id text PRIMARY KEY,
        name text,
        url text,
        actor_id int,
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)
    )
```

3. Payload Table:
Used to store data related to payloads or data associated with events, such as JSON data sent with the event. Includes fields like push ID, size, distinct size, actor ID, and a foreign key constraint on actor_id.
```bash
    CREATE TABLE IF NOT EXISTS payload (
        push_id text PRIMARY KEY,
        size text,
        distinct_size text,
        actor_id int,
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)
    )
```
4. Actors Table:
Used to store data related to actors or individuals who perform the events, such as ID, login, display login, gravatar ID, URL, avatar URL, and other relevant data.

```bash
    CREATE TABLE IF NOT EXISTS actors (
        id int PRIMARY KEY,
        login text,
        display_login text,
        gravatar_id text,
        url text,
        avatar_url text
```


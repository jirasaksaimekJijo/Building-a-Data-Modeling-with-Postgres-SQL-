from typing import NewType
import psycopg2

PostgresCursor = NewType("PostgresCursor", psycopg2.extensions.cursor)
PostgresConn = NewType("PostgresConn", psycopg2.extensions.connection)

table_drop_events = "DROP TABLE IF EXISTS events"
table_drop_actors = "DROP TABLE IF EXISTS actors"

table_create_actors = """
    CREATE TABLE IF NOT EXISTS actors (
        id int PRIMARY KEY,
        login text,
        display_login text,
        gravatar_id text,
        url text,
        avatar_url text
    )
"""

table_create_events = """
    CREATE TABLE IF NOT EXISTS events (
        id text PRIMARY KEY,
        type text,
        actor_id int,
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)
    )
"""

table_create_repo = """
    CREATE TABLE IF NOT EXISTS repo (
        id text PRIMARY KEY,
        name text,
        url text,
        actor_id int,
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)
    )
"""

table_create_payload = """
    CREATE TABLE IF NOT EXISTS payload (
        push_id text PRIMARY KEY,
        size text,
        distinct_size text,
        actor_id int,
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)
    )
"""

create_table_queries = [
    table_create_actors,
    table_create_events,
    table_create_repo,
    table_create_payload,
]
drop_table_queries = [
    table_create_actors,
    table_create_events,
    table_create_repo,
    table_create_payload,
]


def drop_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()
    drop_tables(cur, conn)
    create_tables(cur, conn)
    conn.close()

if __name__ == "__main__":
    main()

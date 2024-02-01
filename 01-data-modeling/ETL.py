import glob
import json
import os
from typing import List

import psycopg2


def get_files(filepath: str) -> List[str]:
    """
    Description: This function is responsible for listing the files in a directory
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print(f"{num_files} files found in {filepath}")

    return all_files

def process(cur, conn, filepath):
    # Get list of files from filepath
    all_files = get_files(filepath)

    for datafile in all_files:
        with open(datafile, "r") as f:
            data = json.loads(f.read())
            for each in data:
                # Print some sample data
                
                if each["type"] == "PushEvent":
                    print(
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["login"],
                        each["actor"]["display_login"],
                        each["actor"]["gravatar_id"],
                        each["actor"]["url"],
                        each["actor"]["avatar_url"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["repo"]["url"],
                        each["created_at"],
                    )  
                    if "payload" in each:
                        # Accessing "push_id" from the first commit in the commits array
                        if "commits" in each["payload"] and len(each["payload"]["commits"]) > 0:
                            each["payload"]["commits"][0]["sha"]
                            each["payload"]["commits"][0]["author"]["email"]
                            each["payload"]["commits"][0]["message"]
                else:
                    print(
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["login"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["created_at"],
                    )

                # Insert data into tables here
                insert_statement = f"""
                    INSERT INTO actors (
                        id,
                        login,
                        display_login,
                        gravatar_id,
                        url,
                        avatar_url
                    ) VALUES ({each["actor"]["id"]}, '{each["actor"]["login"]}', '{each["actor"]["display_login"]}', '{each["actor"]["gravatar_id"]}', '{each["actor"]["url"]}', '{each["actor"]["avatar_url"]}')
                    ON CONFLICT (id) DO NOTHING
                """
                # print(insert_statement)
                cur.execute(insert_statement)

                # Insert data into tables here
                insert_statement = f"""
                    INSERT INTO events (
                        id,
                        type,
                        actor_id
                    ) VALUES ('{each["id"]}', '{each["type"]}', '{each["actor"]["id"]}')
                    ON CONFLICT (id) DO NOTHING
                """
                cur.execute(insert_statement)

                insert_statement = f"""
                    INSERT INTO repo (
                        id,
                        name,
                        url,
                        actor_id
                    ) VALUES (
                        '{each["repo"]["id"]}',
                        '{each["repo"]["name"]}',
                        '{each["repo"]["url"]}',
                        '{each["actor"]["id"]}'
                    ) ON CONFLICT (id) DO NOTHING
                """

                commit_sha = each["payload"]["commits"][0]["sha"] if ("payload" in each and "commits" in each["payload"] and each["payload"]["commits"]) else ''
                payload_size = each["payload"]["size"] if ("payload" in each and "size" in each["payload"]) else ''
                payload_distinct_size = each["payload"]["distinct_size"] if ("payload" in each and "distinct_size" in each["payload"]) else ''
                actor_id = each["actor"]["id"] if ("actor" in each and "id" in each["actor"]) else ''

                cur.execute(insert_statement)

                insert_statement = f"""
                    INSERT INTO payload (
                        push_id,
                        size,
                        distinct_size,
                        actor_id
                    ) VALUES (
                        '{commit_sha}',
                        '{payload_size}',
                        '{payload_distinct_size}',
                        '{actor_id}'
                    ) ON CONFLICT (push_id) DO NOTHING
                """
                cur.execute(insert_statement)

                conn.commit()


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

    process(cur, conn, filepath="../data")

    conn.close()


if __name__ == "__main__":
    main()

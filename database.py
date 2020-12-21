"""
Database functionality
"""
import sqlite3
from typing import Tuple, Dict, List
import utilities as util





def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    connection.commit()
    cursor.close()
    connection.close()


def create_all_jobs_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS main.all_jobs(
            id INTEGER PRIMARY KEY,
            title TEXT,
            company TEXT,
            description TEXT,
            link TEXT,
            category TEXT,
            location TEXT,
            created_at TEXT
        );''')


def insert_into_all_jobs_table(cursor: sqlite3.Cursor, data: List[Dict]):
    print("\nDB:\n---\nInserting results into jobs database...")
    # Clear Previous Entries
    cursor.execute('''DELETE FROM all_jobs''')

    # Re-populate with fresh data
    for job in data:
        title = job["title"]
        company = job["company"]
        desc = job["description"]
        link = job["url"]
        category = job["category"]
        location = job["location"]
        created_at = job["created_at"]

        desc = util.strip_job_description_extras(desc)

        cursor.execute('''INSERT INTO all_jobs (title, company, description, link, category, location, created_at)
                          VALUES(?, ?, ?, ?, ?, ?, ?)''', (title, company, desc, link, category, location, created_at))

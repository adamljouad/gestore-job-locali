import sqlite3
import json
from datetime import datetime
from db import get_connection

def add_job(job_type, payload_dict):
    conn = get_connection()
    c = conn.cursor()
    payload_text = (json.dumps(payload_dict))
    status = "pending"
    created_at = datetime.now().isoformat()

    c.execute(
        """
        INSERT INTO jobs (job_type, payload, status, created_at)
        VALUES (?,  ?, ?, ?)
        """,
        (job_type, payload_text, status, created_at)
    )

    conn.commit()
    job_id = c.lastrowid
    conn.close()

    return job_id

def cli_add_job():
    print("CREA UN NUOVO JOB")
    job_type = input("Tipo di job: ")
    payload_raw = input("Payload JSON: ")

    try:
        payload_dict = json.loads(payload_raw)
    except json.JSONDecodeError:
        print("Errore: il payload non è un JSON")
        return
    
    job_id = add_job(job_type, payload_dict)
    print(f"Job creato con id {job_id}")

if __name__ == "__main__":
    cli_add_job()
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from datetime import datetime
import random
from db import get_db_connection , create_table, create_database


app = FastAPI()

mapp = {}
date_time = {}
def generate_id():
    return str(random.randint(1000,9999))

create_database()
create_table()

@app.get("/create")
def create(url: str):
    short_id = generate_id()

    db = get_db_connection()
    if db is None:
        return {"error":"Database connection failed"}
    short_url = f"http://127.0.0.1:8000/{short_id}"
    cursor = db.cursor()

    insert_query = """
    insert into url_shortner(url,short_id,short_url,created_at) values (%s,%s,%s,%s);
    """
    
    
    cursor.execute(insert_query,(url,short_id,short_url,datetime.now()))
    db.commit()

    cursor.close()
    db.close()
    
    return {
        "short_url": short_url
    }

@app.get("/{short_id}")
def redirect(short_id: str):

    db = get_db_connection()
    if db is None:
        return{"error":"database connect failed"}
    cursor = db.cursor()

    select_query = """ 
    select url,created_at from url_shortner where short_id = %s
    """
    cursor.execute(select_query,(short_id,))

    result = cursor.fetchone()
    if result is None:
        cursor.close()
        db.close()
        return {
            "error":"URL not found"
        }
    original_url = result[0]
    created_at = result[1]

    now = datetime.now()
    if (now - created_at).total_seconds() > 60:
        del_query = "DELETE FROM url_shortner WHERE short_id = %s"
        cursor.execute(del_query,(short_id,))
        db.commit()

        cursor.close()
        db.close()
        return {"Error":"URL Expires"}
    
    cursor.close()
    db.close()
    return RedirectResponse(url=original_url)

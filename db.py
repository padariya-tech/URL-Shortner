import mysql.connector


def get_db_connection():

    db = mysql.connector.connect(
        unix_socket="/tmp/mysql.sock",
        user="root",
        password="",
        database="url_shortner"
    )

    return db


def create_database():

    db = mysql.connector.connect(
        unix_socket="/tmp/mysql.sock",
        user="root",
        password=""
    )

    cursor = db.cursor()

    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS url_shortner"
    )

    db.commit()

    cursor.close()
    db.close()


def create_table():

    db = get_db_connection()

    cursor = db.cursor()

    c_table = """
    CREATE TABLE IF NOT EXISTS url_shortner(
        id INT PRIMARY KEY AUTO_INCREMENT,
        url TEXT NOT NULL,
        short_id VARCHAR(64) NOT NULL,
        short_url VARCHAR(64) NOT NULL,
        created_at DATETIME NOT NULL
    )
    """

    cursor.execute(c_table)

    db.commit()

    cursor.close()
    db.close()
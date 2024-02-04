import sqlite3
import logging


def db_connection(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("todo.db")
        cu = conn.cursor()

        kwargs["cursor"] = cu
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logging.error(e)
        finally:
            conn.commit()
            conn.close()

        return result

    return wrapper


@db_connection
def create_table(cursor):
    cursor.execute(
        """CREATE TABLE tasks (
        content TEXT NOT NULL,
        priority INT NOT NULL)"""
    )


@db_connection
def add_task(content, priority, cursor):
    cursor.execute(
        """INSERT INTO tasks VALUES
        (?, ?)
        """,
        (content, priority),
    )


@db_connection
def show_tasks(cursor):
    cursor.execute("SELECT rowid, * FROM tasks")
    data = cursor.fetchall()
    return data
    


@db_connection
def remove_task(rowid, cursor):
    cursor.execute("DELETE FROM tasks WHERE rowid = ?", (rowid,))


@db_connection
def update_task(rowid, content, priority, cursor):
    cursor.execute(
        """UPDATE tasks 
        SET 
        content = COALESCE(?, content),
        priority = COALESCE(?, priority)
        WHERE rowid = ? 
        """,
        (content, priority, rowid),
    )

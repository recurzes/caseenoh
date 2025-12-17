
import sqlite3
def get_connections():
    return(
        sqlite3.connect(r"casino.db")
    )
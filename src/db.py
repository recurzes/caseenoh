
import sqlite3
def get_connections():
    return(
        sqlite3.connect(r"C:\Users\Jethro\Desktop\CasinoDatabase\casino")
    )

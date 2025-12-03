import mysql.connector
def get_connection():
    return (
        mysql.connector.connect(
        host="localhost",
        user="root",
        password="kalamomagandaka076",
        port="3306",
        database="casino_app"
    ))
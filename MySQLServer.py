# MySQLServer.py
import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Connects to the MySQL server and creates the 'alx_book_store' database
    if it doesn't already exist.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Use IF NOT EXISTS to prevent an error if the database already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

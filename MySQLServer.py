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
        # Establish connection to MySQL server
        # IMPORTANT: Replace 'your_username' and 'your_password' with your actual MySQL credentials
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # SQL statement to create the database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # Print success message
            print("Database 'alx_book_store' created successfully! 🎉")

    except Error as e:
        # Handle connection and database creation errors
        print(f"Error connecting to MySQL: {e} ❌")

    finally:
        # Ensure cursor and connection are closed
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed. 👋")

if __name__ == "__main__":
    create_database()

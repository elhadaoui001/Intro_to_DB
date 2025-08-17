# MySQLServer.py

import mysql.connector
from mysql.connector import Error
import getpass

def create_database():
    try:
        # Prompt user for MySQL credentials
        user = input("Enter MySQL username: ")
        password = getpass.getpass("Enter MySQL password: ")

        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user=Hamza,
            password=123456AZEnb@@/
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()

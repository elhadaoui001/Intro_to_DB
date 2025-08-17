#!/usr/bin/python3
"""
A simple Python script to create the 'alx_book_store' database
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (adjust user & password to your setup)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # <-- replace with your MySQL username
            password="password" # <-- replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection closed.")  # optional

if __name__ == "__main__":
    create_database()

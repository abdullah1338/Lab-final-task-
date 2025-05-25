import mysql.connector
from mysql.connector import Error


def create_database():
    connection = None  # Initialize connection variable
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS hospital_management")
            cursor.execute("USE hospital_management")

            # Create tables
            tables = [
                """CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    role ENUM('admin', 'doctor', 'staff') NOT NULL
                )""",
                """CREATE TABLE IF NOT EXISTS patients (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    dob DATE NOT NULL,
                    gender ENUM('Male', 'Female', 'Other') NOT NULL,
                    address TEXT,
                    phone VARCHAR(20),
                    email VARCHAR(100),
                    registered_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )""",
                # ... (include all other table creation queries from previous example)
            ]

            for table in tables:
                try:
                    cursor.execute(table)
                except Error as e:
                    print(f"Error creating table: {e}")

            print("Database and tables created successfully")

    except Error as e:
        print(f"MySQL Error: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure MySQL server is running")
        print("2. Verify your username and password")
        print("3. Check if MySQL service is running (services.msc)")
        print("4. Try '127.0.0.1' instead of 'localhost' if having connection issues")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")


if __name__ == "__main__":
    create_database()
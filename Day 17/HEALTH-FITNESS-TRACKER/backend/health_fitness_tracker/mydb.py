import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MySQL credentials from environment variables
mysql_password = os.getenv("MYSQL_PASSWORD")


# Connect to MySQL database
data_base = mysql.connector.connect(
    host="localhost",
    user="root",
    password=mysql_password,
)

cursor_object = data_base.cursor()

cursor_object.execute("CREATE DATABASE IF NOT EXISTS health_fitness_tracker")

cursor_object.execute("USE health_fitness_tracker")

print("Database connected successfully!")
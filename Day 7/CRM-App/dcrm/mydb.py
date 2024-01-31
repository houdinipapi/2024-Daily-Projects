import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1234@adMIN",
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
print("Database created successfully.")
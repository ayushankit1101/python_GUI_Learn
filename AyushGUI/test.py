import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "7266",
    database = "login_info"
)

cur = mydb.cursor()
query = "INSERT INTO user_data VALUES ()"
cur.execute(query)

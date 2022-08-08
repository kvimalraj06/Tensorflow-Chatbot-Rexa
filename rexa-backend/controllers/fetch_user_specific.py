import mysql.connector

"""DB configuration"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ofsthozhan"
)

def fetch_details(username):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM employeedetails")
    details = mycursor.fetchall()
    mycursor.execute("select Column_name from Information_schema.columns where Table_name like 'employeedetails'")
    headers = mycursor.fetchall()
    mydb.commit()
    user_details = {}
    print(len(headers))
    for i in range(len(headers)):
        user_details[headers[i][0]] = details[0][i]
    return user_details
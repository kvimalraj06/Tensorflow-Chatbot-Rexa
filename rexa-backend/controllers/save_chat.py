import mysql.connector

"""DB configuration"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ofsthozhan"
)

def save(user_chat,bot_response):
    mycursor = mydb.cursor()

    sql_query = "INSERT INTO chathistory (userid, userchat, botresponse) VALUES (%s, %s, %s)"
    params = (1, user_chat, bot_response)
    mycursor.execute(sql_query, params)

    mydb.commit()
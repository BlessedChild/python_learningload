import mysql.connector

cnx = mysql.connector.connect(user='root', password='88888888', host='127.0.0.1', database='my_db')
cursor = cnx.cursor()

query = ("SELECT * FROM Account ")

cursor.execute(query)

for (ID, AccountName, Password) in cursor:
  print("{}, {}, {}".format(
    ID, AccountName, Password))

cursor.close()
cnx.close()


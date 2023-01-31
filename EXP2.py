import mysql.connector
mydb = mysql.connector.connect(host="localhost", port='3307', user="root", password="")
#print(mydb)
if (mydb):
    print("connection done")
else:
    print("connection error")

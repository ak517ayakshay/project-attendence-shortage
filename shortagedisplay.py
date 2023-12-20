import mysql.connector
from prettytable import PrettyTable
import emailsender
import tkinteremail

def mainprgm1():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="P@ssw0rd@4321",
        database="akshay"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM stdet WHERE attper <= 60;"

    mycursor.execute(sql)
    results = mycursor.fetchall()

    table = PrettyTable()
    table.field_names = [desc[0] for desc in mycursor.description]

    print("\n\n\n       THE LIST OF ATTENDANCE SHORTAGE STUDENT\n\n")
    for row in results:
        table.add_row(row)

    print(table)
    
    print("\n\nPress 1 if you want to send email")
    n = input()
    
    if n == '1':  
        print("Sending emails...")
        sql = "SELECT namee, email, attper FROM stdet WHERE attper <= 60;"
        mycursor.execute(sql)
        ret = mycursor.fetchall()
        
        for i in ret:
            emailsender.mainprgm(i[1], i[0], i[2])
            print(f"email sent to {i[0]}")

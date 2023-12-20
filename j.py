import mysql.connector
import tkinter as tk
from tkinter import messagebox
from prettytable import PrettyTable
import emailsender

def fetch_students():
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

    for row in results:
        table.add_row(row)

    return table

def send_emails():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="P@ssw0rd@4321",
        database="akshay"
    )

    mycursor = mydb.cursor()
    sql = "SELECT namee, email, attper FROM stdet WHERE attper <= 60;"
    mycursor.execute(sql)
    students = mycursor.fetchall()

    for student in students:
        emailsender.mainprgm(student[1], student[0], student[2])

def show_attendance_list():
    table = fetch_students()
    messagebox.showinfo("Attendance List", table)

def send_emails_buffer():
    send_emails()
    messagebox.showinfo("Emails Sent", "Emails have been sent successfully.")

# Tkinter GUI
root = tk.Tk()
root.title("Email Sender Application")

fetch_button = tk.Button(root, text="Fetch Attendance List", command=show_attendance_list)
fetch_button.pack(pady=10)

send_button = tk.Button(root, text="Send Emails", command=send_emails_buffer)
send_button.pack(pady=10)

root.mainloop()

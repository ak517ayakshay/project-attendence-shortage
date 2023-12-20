def mainprgm():
    import mysql.connector

    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="P@ssw0rd@4321",
    database="akshay"
    )
    mycursor = mydb.cursor()
    # mycursor.execute("CREATE TABLE stdet (usn VARCHAR(11) UNIQUE PRIMARY KEY, namee VARCHAR(15), email VARCHAR(150), clasattended INT default 0, attper DECIMAL(5,2))")
    # mycursor.execute("CREATE TRIGGER atendiper BEFORE UPDATE ON stdet FOR EACH ROW SET NEW.attper = (NEW.clasattended * 100) / 60")

    n=int(input("enter number of students whose details you are going to enter"))
    for i in range(n):
        usn = input("Enter USN of student: ")
        namee = input("Enter name of student: ")
        email = input("Enter email of student: ")
        classattended = input("Enter number of classes attended: ")
        
        sql = "INSERT INTO stdet (usn, namee, email, clasattended) VALUES (%s, %s, %s, %s)"
        val = (usn, namee, email, classattended)
        mycursor.execute(sql, val)
        mycursor.execute("update stdet set attper = (clasattended*100)/60")
        mydb.commit()
        print("added student successfully")



def mainprgm(reciverr,name,attendance_percentage):
    import smtplib
    # simple mail transer proto
    email ="legendguyreports@gmail.com"
    # reciver = input("enter reciver")

    subject="Attendance Warning"
    message=f"Dear {name},\n\nYour attendance is below 60% ({attendance_percentage}%).\nPlease attend classes regularly to improve your attendance.\n\nSincerely,\nThe Attendance System"


    text=f"Subject:{subject} \n\n {message}"

    server=smtplib.SMTP("smtp.gmail.com",587)
    # 587 is default port for tls to get activated tls means transfer layer security which helps you to transfer safely it replaced secure socket layer tech which is obsalate
    server.starttls()
    # here server is smtp.gmail.com
    server.login(email,"bltosyznxhklaydz")
    # tht is ur apppassword "" one
    server.sendmail(email,reciverr,text)

    
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("abhikesare9@gmail.com","*****")
server.sendmail("abhikesare9@gmail.com","muktakesare9@gmail.com","Face found of abhishek")
server.quit()
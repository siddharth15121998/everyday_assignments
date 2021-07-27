import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("chavala.sridhar476@gmail.com","Sridhar123@")
message="hello"
connection.sendmail("chavala.sridhar476@gmail.com","chavala.renuka@gmail.com",message)
print("sent")
connection.quit()
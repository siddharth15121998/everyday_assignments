import smtplib
inputnumber=list(map(int,input("Enter the number").split()))
even= list(filter(lambda x: (x % 2 == 0), inputnumber)) 
print(even)
message=""
message=' '.join(map(str, even))
print(message)
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("balu08062000@gmail.com","balu@123")
connection.sendmail("balu08062000@gmail.com","balusaravanan862@gmail.com",message)
connection.quit
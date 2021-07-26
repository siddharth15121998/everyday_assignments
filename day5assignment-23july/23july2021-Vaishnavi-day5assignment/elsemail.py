import smtplib
li=[]
even=[]
l=int(input("Enter a number: "))
for i in range(10):
    n=int(input("Enter a number: "))
    li.append(n)
for n in li:
    if(n%2==0):
        even.append(n)
message = ' '.join(map(str,even))
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
connection.sendmail("vaishnavi.p6521@gmail.com","priya.hajela358@gmail.com",message)
print("email has successfully send")
connection.quit()
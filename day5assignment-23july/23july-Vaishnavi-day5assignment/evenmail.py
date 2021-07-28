import smtplib
li=[]
n=int(input("enter the number : "))
for i in range(10):
    element=int(input("enter the number : "))
    li.append(element)
print(li)
even=[]
odd=[]
for i in range(len(li)):
    if(li[i]%2==0):
        even.append(li[i])
    else:
        odd.append(li[i])
print(even)
print(odd)
messages = ' '.join([str(elem) for elem in even])
print(messages)
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
connection.sendmail("vaishnavi.p6521@gmail.com","priya.hajela358@gmail.com",messages)
print("message is successfully send")
connection.quit()


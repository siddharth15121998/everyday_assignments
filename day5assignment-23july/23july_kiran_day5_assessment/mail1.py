import smtplib
li=[]
n=int(input("enter numbers:"))
for i in range(n):
    element=int((input("enter the number:")))
    li.append(element)
print(li)
even=[]
odd=[]
for i in range (len(li)):
    if(li[i]%2==0):
        even.append(li[i])
    else:
        odd.append(li[i])
print(even)
print(odd)
message=' '.join([str(elem) for elem in even])
print(message)
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("969kiran969@gmail.com","Kiran@969")
message="hello good morning"
connection.sendmail("969kiran969@gmail.com","rachapallikirankumar969@gmail.com",message)
print("message sent")
connection.quit()
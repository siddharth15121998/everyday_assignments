import smtplib
n = int(input())
l = []
even =[]
odd=[]
for i in range(n):
    num = int(input())
    l.append(num)
print(l)
for i in range(len(l)):
    if(list[i]%2==0):
        even.append(list[i])
    else:
        odd.append(l[i])
message = ' '.join([str(i) for i in even])
print(message)
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("Arifkhan0786@gmail.com","Absrkhan078621")
connection.sendmail("Arifkhan0786@gmail.com","barfikhan78621@gmail.com",message)
connection.quit()
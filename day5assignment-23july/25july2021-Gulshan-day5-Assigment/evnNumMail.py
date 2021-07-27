import smtplib
# string = input('enter the string')
# s = string.upper()
n = int(input())
l = []
even =[]
odd=[]
for i in range(n):
    num = int(input())
    l.append(num)
print(l)
for i in range(len(l)):
    if(l[i]%2==0):
        even.append(l[i])
    else:
        odd.append(l[i])
message = ' '.join([str(i) for i in even])
#message =' '.join(map(str, even))
print(message)
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("gulshan062132@gmail.com","Gullu@2132")
# message=s[0:5]
connection.sendmail("gulshan062132@gmail.com","gulshankumar060699@gmail.com",message)
connection.quit()
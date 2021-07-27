import smtplib
li=[]
evenmsg=[]
for i in range(10):
    n=int(input("Enter the number :"))
    li.append(n)
for num in li:
    if(num%2==0):
        evenmsg.append(num)
msg=' '.join(map(str,evenmsg))
# print(msg)
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("ridhimathur10@gmail.com","ridhima@10")
#msg="Hello there , good evening"
connection.sendmail("ridhimathur10@gmail.com","hariompateldada@gmail.com",msg)
print("email has successfully send")
connection.quit()
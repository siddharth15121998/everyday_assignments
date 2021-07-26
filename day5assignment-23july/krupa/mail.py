import smtplib
#from email.mime.image import MIMEImage
li=[]
n=int(input("enter the no:"))
for i in range(n):
        element=int(input("enter the number"))
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
messages=' '.join([str(elem)fot elem in even])
print(messages)


connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("krupamh0@gmail.com","panipuri23@")
message="hello"
connection.sendmail("krupa2332@gmail.com","krupa9927@gmail.com",message)
print("email has sent")
connection.quit()

#with open('Screenshot(32).png', 'rb') as fp:
#         img = MIMEImage(fp.read())
#         img.add_header('Content-Disposition', 'attachment', filename="Screenshot(32).png")
#         msg.attach(img)


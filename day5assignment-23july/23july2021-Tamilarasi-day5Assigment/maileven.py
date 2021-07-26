import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587) #connection smtp
connection.starttls()
connection.login("tamilarasiiprimed@gmail.com","Iprimed@123") 
n1=int(input("Enter the Num:"))
even=""
for i in range(9):
    n=int(input())
    if n%2==0:
        even=even+' '+str(n)
message=even
connection.sendmail("tamilarasiiprimed@gmail.com","tamilarasiifet@gmail.com",message) 
print("mail send successfully")
connection.quit()
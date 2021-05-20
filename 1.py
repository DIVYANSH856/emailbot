import mysql.connector
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mydb=mysql.connector.connect( host="localhost",password="Sh!p",user='root',database='emailbot')
mycursor=mydb.cursor()
sql = "select email_adress from subscribers"
mycursor.execute(sql)
a=mycursor.fetchall()
print(a)
b=len(a)
sender_email="kohlidivyansh122@gmail.com"
rec_email=''
password=input(str("please enter your password"))
context = ssl.create_default_context()
message = MIMEMultipart("alternative")
message['subject']="MULTIPART TEST"
message['from']=sender_email
message['to']=rec_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
check latest price of dogecoin:
https://www.coindesk.com/price/dogecoin"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       check latest price of <a href="https://www.coindesk.com/price/dogecoin">DOGECOIN</a> 
    </p>
  </body>
</html>
"""
# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)



try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    print('login success')
    for i in range(b):
      rec_email=a[i][0]
      server.sendmail(sender_email, rec_email, message.as_string())
      print('email has been sent to',rec_email)
except Exception as e:
    print(e)

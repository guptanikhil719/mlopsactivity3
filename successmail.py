import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "guptanikhil719@gmail.com"
host_pass = "Nikhil@94588"
guest_address = "guptanikhil719@gmail.com"
subject = "Regarding Success of your model "
content = '''Hello, 
				Dear Developer your model has achieved the desired accuracy.
			THANK YOU ...'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')
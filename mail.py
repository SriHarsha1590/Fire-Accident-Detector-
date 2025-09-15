import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
port = 465  
smtp_server = "smtp.gmail.com"
sender_email = "sriharshaa1590@gmail.com" 
receiver_email = "cmsh800@gmail.com"  
password = "vtzb qkso oryn hubo "
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "It's Urgent"
body = "The Fire is Spreading near Your House"
message.attach(MIMEText(body, "plain"))

context = ssl.create_default_context()

def send_email():
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred while sending email: {e}")

from email.message import EmailMessage
import ssl
import smtplib


email_sender = "mmitchell3368@gmail.com"
email_password = 'nlcdnxkhxladvups'
email_receiver = 'mmitchell3368@gmail.com'

subject = 'Check out my GitHub account!'

body = '''
I've just added new projects: https://github.com/mmitchell3368
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


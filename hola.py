from email.message import EmailMessage

import ssl
import smtplib

email_sender = 'alexvelandry@gmail.com'
email_password = 'ziqn hvrx keus hogd'

email_receiver = 'alexmarcus10@gmail.com'

subject = "Prueba de correo"

body = """Hola Alex esta es una prueba para el correo electronico"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())
password="ziqn hvrx keus hogd"
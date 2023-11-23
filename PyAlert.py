import os
import smtplib
import ssl
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from hola import password
from email.message import EmailMessage

_name_ = input("Para empezar escribe START")
# Configuración de la carpeta a auditar y las credenciales del correo electrónico
folder_to_watch = r'C:\Users\alexm\Documents\Auditar'
email_sender = 'alexvelandry@gmail.com'
email_password = password
email_recipient = 'alexmarcus10@gmail.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

class FolderEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        new_file = event.src_path
        print(f"Nuevo archivo agregado: {new_file}")

        # Envía un correo electrónico
        send_email(new_file)

def send_email(attachment_path):
    # Configura el servidor SMTP
    

    # Configura el correo electrónico
    subject = 'Nueva actualización en la carpeta'
    body = 'Se ha agregado un nuevo archivo. ' + attachment_path
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_recipient
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender,email_recipient, em.as_string())

def main():
    event_handler = FolderEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=False)
    observer.start()

    try:
        print(f"Auditando la carpeta: {folder_to_watch}")
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if _name_ == "START":
    main()
else:
    exit()

from typing import List, Tuple
from aurous79 import app, init_mail
from aurous79.extension import SessionLocal
from flask_mail import Message
from aurous79.models import EmailLibrary


def send_batch_emails_from_email_lib(email_subject: str, email_content: str) -> bool:
    session: SessionLocal = SessionLocal()
    # if email library is empty - return false
    email_library: List[Tuple[str]] = session.query(EmailLibrary.email).first()
    if email_library is None:
        return False
    # if email exists send message to recipients
    email_library: List[Tuple[str]] = session.query(EmailLibrary.email).all()    # returns a list of tuples
    email_recipients: List[str] = []
    # convert tuple to list 
    for customer in email_library:
        email_recipients.append(customer)
    msg = Message(f"{email_subject}", recipients=email_recipients)
    msg.body: str = f"{email_content}\n\n"
    with app.open_resource("aurouslogo.jpg") as logo:
        msg.attach("aurouslogo.jpg", "image/jpg", logo.read())
    mail = init_mail(app)
    mail.send(msg)
    return True
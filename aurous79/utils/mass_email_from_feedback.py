from typing import List, Tuple
from aurous79 import app, init_mail
from aurous79.extension import SessionLocal
from flask_mail import Message
from aurous79.models import FeedbackForm

mail = init_mail(app)


def send_batch_emails_from_feedback(email_subject: str, email_content: str) -> bool:
    session: SessionLocal = SessionLocal()
    # if feedback email is empty - return false
    feedback_email: List[Tuple[str]] = session.query(FeedbackForm.email).first()
    if feedback_email is None:
        return False
    # if email exists send message to recipients
    feedback_emails: List[Tuple[str]] = session.query(
        FeedbackForm.email
    ).all()  # returns a list of tuples
    print(feedback_email)
    email_recipients: List[str] = []
    # convert tuple to list
    for customer in feedback_emails:
        email_recipients.append(customer[0])
    msg = Message(f"{email_subject}", recipients=email_recipients)
    msg.body: str = f"{email_content}\n\n"
    with app.open_resource("aurouslogo.jpg") as logo:
        msg.attach("aurouslogo.jpg", "image/jpg", logo.read())
    mail.send(msg)
    return True

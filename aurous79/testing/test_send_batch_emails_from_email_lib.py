import pytest
from datetime import datetime
from aurous79 import app, init_mail
from aurous79.extension import SessionLocal
from aurous79.testing.client import client
from aurous79.models import EmailLibrary
from aurous79.utils.create_feedback import create_feedback
from aurous79.utils.mass_email_from_email_library import send_batch_emails_from_email_lib


def test_send_batch_emailLibrary_emails():
    """Create feedback and send emails to them"""
    session: SessionLocal = SessionLocal()
    # create 3x feedback forms
    customer1: EmailLibrary = EmailLibrary(
        name="John Doe",
        email="john@email.com",
        timestamp=datetime.now(),
    )
    customer1_feedback: EmailLibrary = create_feedback(
        name=customer1.name,
        email=customer1.email,
    )

    customer2: EmailLibrary = EmailLibrary(
        name="Jane Doe",
        email="jane@email.com",
    )
    customer2_feedback: EmailLibrary = create_feedback(
        name=customer2.name,
        email=customer2.email,
    )

    customer3: EmailLibrary = EmailLibrary(
        name="Max Jones",
        email="max@email.com",
    )
    customer3_feedback: EmailLibrary = create_feedback(
        name=customer3.name,
        email=customer3.email,
    )

    with app.app_context():
        mail = init_mail(app)
        with mail.record_messages() as outbox:
            email_subject = "Test Email Subject"
            email_content = "Test Email Content"
            sent_email: bool = send_batch_emails_from_email_lib(email_subject, email_content)
            
            # check if emails were sent
            # assert sent_email is True

#             # check if outbox object exists
#             assert len(outbox) == 1
#             assert outbox[0].subject == email_subject
#             assert outbox[0].recipients == [customer1.email, customer2.email, customer3.email]
#             assert email_content in outbox[0].body
#             assert outbox[0].body == f"{email_content}\n\n"
        
    
    # remove db data
    session.delete(customer1_feedback)
    session.delete(customer2_feedback)
    session.delete(customer3_feedback)
    session.commit()

    with app.app_context():
        get_feedback: EmailLibrary = EmailLibrary.query.all()
        assert len(get_feedback) == 0
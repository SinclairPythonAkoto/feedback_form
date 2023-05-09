import pytest
from datetime import datetime
from aurous79 import app, init_mail
from aurous79.extension import SessionLocal
from aurous79.testing.client import client
from aurous79.models import EmailLibrary
from aurous79.utils.add_to_email_library import add_to_email_library
from aurous79.utils.create_feedback import create_feedback
from aurous79.utils.mass_email_from_email_library import send_batch_emails_from_email_lib
from aurous79.utils.create_email import send_one_email


def test_send_single_email():
    """Check if email is sent to given recipient"""
    
    with app.app_context():
        mail = init_mail(app)
        with mail.record_messages() as outbox:
            email: str = "john@email.com"
            email_subject: str = "Test subject"
            email_content: str = "Test content"
            sent_email: bool = send_one_email(email, email_subject, email_content)

            # check if email has been sent
            assert sent_email is True

            # check if outbox object exists
            assert len(outbox) == 1
            assert outbox[0].subject == email_subject
            assert outbox[0].recipients == [email]
            assert email_content in outbox[0].body
            assert outbox[0].body == f"{email_content}\n\n"

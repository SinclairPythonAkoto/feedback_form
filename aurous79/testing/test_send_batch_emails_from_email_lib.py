import pytest
from datetime import datetime
from aurous79 import app, init_mail
from aurous79.extension import SessionLocal
from aurous79.testing.client import client
from aurous79.models import EmailLibrary
from aurous79.utils.add_to_email_library import add_to_email_library
from aurous79.utils.create_feedback import create_feedback
from aurous79.utils.mass_email_from_email_library import (
    send_batch_emails_from_email_lib,
)


def test_send_batch_emailLibrary_emails():
    """Create feedback and send emails to them"""
    session: SessionLocal = SessionLocal()
    # create 3x feedback forms
    customer1: EmailLibrary = EmailLibrary(
        customer_name="John Doe",
        customer_email="john@email.com",
    )
    new_customer1: EmailLibrary = add_to_email_library(
        name=customer1.customer_name,
        email=customer1.customer_email,
    )

    customer2: EmailLibrary = EmailLibrary(
        customer_name="Jane Doe",
        customer_email="jane@email.com",
    )
    new_customer2: EmailLibrary = add_to_email_library(
        name=customer2.customer_name,
        email=customer2.customer_email,
    )

    customer3: EmailLibrary = EmailLibrary(
        customer_name="Max Jones",
        customer_email="max@email.com",
    )
    new_customer3: EmailLibrary = add_to_email_library(
        name=customer3.customer_name,
        email=customer3.customer_email,
    )

    with app.app_context():
        mail = init_mail(app)
        with mail.record_messages() as outbox:
            email_subject = "Test Email Subject"
            email_content = "Test Email Content"
            sent_email: bool = send_batch_emails_from_email_lib(
                email_subject, email_content
            )

            # check if emails were sent
            assert sent_email is True

            # check if outbox object exists
            assert len(outbox) == 1
            assert outbox[0].subject == email_subject
            assert outbox[0].recipients == [
                customer1.customer_email,
                customer2.customer_email,
                customer3.customer_email,
            ]
            assert email_content in outbox[0].body
            assert outbox[0].body == f"{email_content}\n\n"

    # remove db data
    session.delete(new_customer1)
    session.delete(new_customer2)
    session.delete(new_customer3)
    session.commit()

    with app.app_context():
        get_feedback: EmailLibrary = EmailLibrary.query.all()
        assert len(get_feedback) == 0

import pytest
from flask_mail import Message
from datetime import datetime
from aurous79 import app, init_mail
from aurous79.testing.client import client
from aurous79.utils.validate_email import is_email_valid
from aurous79.utils.create_email import send_email


def test_send_automated_email_to_customer():
    """Check if email is sent to customer"""
    email_timestamp: datetime = datetime.now().strftime("%H:%M")
    email_datestamp: datetime = datetime.now().strftime("%d/%m/%Y")

    email: str = "someone@email.com"
    name: str = "John Doe"
    discount: str = "5%"

    with app.app_context():
            mail = init_mail(app)
            with mail.record_messages() as outbox:
                email_sent: bool = send_email(name=name, email=email, discount=discount)

                expected_body: str = (
                    f"Thank you {name} for completing our feedback form! You have earned {discount}"
                    " off from your next bill.\n\nTo gain your discount please show this email to the cashier."
                    f"\n\nPlease note that this expires 24hrs after {email_timestamp}, {email_datestamp}.\n\n\n"
                )

                # check if email was sent
                assert email_sent is True

                assert len(outbox) == 1
                assert outbox[0].subject == f"Aurous79® {discount} Discount!"
                assert outbox[0].recipients == [email]
                assert outbox[0].body == expected_body
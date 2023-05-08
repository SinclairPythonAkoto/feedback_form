from aurous79 import app, init_mail
from flask_mail import Message
from datetime import datetime

mail = init_mail(app)


def send_email(name: str, email: str, discount: str) -> bool:
    """Create an email with a 5% or 10% discount"""
    if not email:
        return False
    
    email_timestamp = datetime.now().strftime("%H:%M")
    email_datestamp = datetime.now().strftime("%d/%m/%Y")

    email_message = Message(f"Aurous79® {discount} Discount!", recipients=[email])
    email_message.body = (
        f"Thank you {name} for completing our feedback form! You have earned {discount}"
        " off from your next bill.\n\nTo gain your discount please show this email to the cashier."
        f"\n\nPlease note that this expires 24hrs after {email_timestamp}, {email_datestamp}.\n\n\n"
    )

    # attach image to email
    with app.open_resource("aurouslogo.jpg") as logo:
        email_message.attach("aurouslogo.jpg", "image/jpeg", logo.read())

    # send email
    mail.send(email_message)
    return True

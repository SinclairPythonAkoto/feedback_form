from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.models import EmailLibrary


def add_to_email_library(name: str, email: str) -> EmailLibrary:
    """Add name & email to Aurous79 email library"""
    with app.app_context():
        session: SessionLocal = SessionLocal()
        new_entry: EmailLibrary = EmailLibrary(
            customer_name=name,
            customer_email=email
        )
        session.add(new_entry)
        session.commit()
    return new_entry
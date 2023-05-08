import pytest
from datetime import datetime
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.testing.client import client
from aurous79.models import FeedbackForm
from aurous79.utils.create_feedback import create_feedback
from aurous79.utils.validate_email import validate_email, find_email


def test_validate_confirmation_email():
    """Check if user email matches confirmation email"""
    # create a valid email
    customer1_email: str = "john@email.com"
    customer1_email_confirmation: str = "john@email.com"
    assert validate_email(customer1_email, customer1_email_confirmation) == True

    # create invalid email
    customer2_email: str = "john@email.com"
    customer2_email_confirmation: str = "jane@email.com"
    assert validate_email(customer2_email, customer2_email_confirmation) == False


def test_find_email(client):
    """Check if email exists in db"""
    # create feeback object
    customer: FeedbackForm = FeedbackForm(
        name="John Doe",
        age=17,
        sex="male",
        first_visit="yes",
        return_visit="yes",
        clean=3,
        service=4,
        speed=5,
        food_quality=3,
        shisha="no",
        comment="First comment",
        email="john@email.com",
        timestamp=datetime.now(),
    )
    new_feedback: FeedbackForm = create_feedback(
        name=customer.name,
        age=customer.age,
        sex=customer.sex,
        first_visit=customer.first_visit,
        return_visit=customer.return_visit,
        clean=customer.clean,
        service=customer.service,
        speed=customer.speed,
        food_quality=customer.food_quality,
        shisha=customer.shisha,
        comment=customer.comment,
        email=customer.email,
    )
    
    # check if email entry exists in db
    assert find_email(customer.email) == True

    # check if random email exists in db
    assert find_email('some_random_email@email.com') == False


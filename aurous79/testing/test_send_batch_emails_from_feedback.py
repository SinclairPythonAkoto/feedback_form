import pytest
from datetime import datetime
from aurous79 import app, init_mail
from aurous79.extension import SessionLocal
from aurous79.testing.client import client
from aurous79.models import FeedbackForm
from aurous79.utils.create_feedback import create_feedback
from aurous79.utils.mass_email_from_feedback import send_batch_emails_from_feedback


def test_send_batch_emails():
    """Create multiple feedback forms and check if exist in db"""
    session: SessionLocal = SessionLocal()
    # create more than feedback form
    customer1: FeedbackForm = FeedbackForm(
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
    customer1_feedback: FeedbackForm = create_feedback(
        name=customer1.name,
        age=customer1.age,
        sex=customer1.sex,
        first_visit=customer1.first_visit,
        return_visit=customer1.return_visit,
        clean=customer1.clean,
        service=customer1.service,
        speed=customer1.speed,
        food_quality=customer1.food_quality,
        shisha=customer1.shisha,
        comment=customer1.comment,
        email=customer1.email,
    )

    customer2: FeedbackForm = FeedbackForm(
        name="Jane Doe",
        age=19,
        sex="female",
        first_visit="no",
        return_visit="yes",
        clean=3,
        service=3,
        speed=4,
        food_quality=4,
        shisha="yes",
        comment="Second comment",
        email="jane@email.com",
        timestamp=datetime.now(),
    )
    customer2_feedback: FeedbackForm = create_feedback(
        name=customer2.name,
        age=customer2.age,
        sex=customer2.sex,
        first_visit=customer2.first_visit,
        return_visit=customer2.return_visit,
        clean=customer2.clean,
        service=customer2.service,
        speed=customer2.speed,
        food_quality=customer2.food_quality,
        shisha=customer2.shisha,
        comment=customer2.comment,
        email=customer2.email,
    )

    customer3: FeedbackForm = FeedbackForm(
        name="Max Jones",
        age=25,
        sex="male",
        first_visit="no",
        return_visit="no",
        clean=3,
        service=3,
        speed=2,
        food_quality=3,
        shisha="no",
        comment="Third comment",
        email="max@email.com",
        timestamp=datetime.now(),
    )
    customer3_feedback: FeedbackForm = create_feedback(
        name=customer3.name,
        age=customer3.age,
        sex=customer3.sex,
        first_visit=customer3.first_visit,
        return_visit=customer3.return_visit,
        clean=customer3.clean,
        service=customer3.service,
        speed=customer3.speed,
        food_quality=customer3.food_quality,
        shisha=customer3.shisha,
        comment=customer3.comment,
        email=customer3.email,
    )

    # get db data
    with app.app_context():
        get_feedback: FeedbackForm = FeedbackForm.query.all()

        # check if 3 db entries created
        assert len(get_feedback) == 3

    with app.app_context():
        mail = init_mail(app)
        with mail.record_messages() as outbox:
            email_subject = "Test Email Subject"
            email_content = "Test Email Content"
            sent_email: bool = send_batch_emails_from_feedback(email_subject, email_content)
            
            # check if emails were sent
            assert sent_email is True

            # check if outbox object exists
            assert len(outbox) == 1
            assert outbox[0].subject == email_subject
            assert outbox[0].recipients == [customer1.email, customer2.email, customer3.email]
            assert email_content in outbox[0].body
            assert outbox[0].body == f"{email_content}\n\n"
        
    
    # remove db data
    session.delete(customer1_feedback)
    session.delete(customer2_feedback)
    session.delete(customer3_feedback)
    session.commit()

    with app.app_context():
        get_feedback: FeedbackForm = FeedbackForm.query.all()
        assert len(get_feedback) == 0
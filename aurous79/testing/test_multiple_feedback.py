import pytest
from datetime import datetime
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.testing.client import client
from aurous79.models import FeedbackForm
from aurous79.utils.create_feedback import create_feedback


def test_create_multiple_feedback(client):
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

        # check customer 1 db entry
        assert customer1.name == get_feedback[0].name
        assert customer1.age == get_feedback[0].age
        assert customer1.sex == get_feedback[0].sex
        assert customer1.first_visit == get_feedback[0].first_visit
        assert customer1.return_visit == get_feedback[0].return_visit
        assert customer1.clean == get_feedback[0].clean
        assert customer1.speed == get_feedback[0].speed
        assert customer1.food_quality == get_feedback[0].food_quality
        assert customer1.shisha == get_feedback[0].shisha
        assert customer1.comment == get_feedback[0].comment
        assert customer1.email == get_feedback[0].email

        # check customer 2 db entry
        assert customer2.name == get_feedback[1].name
        assert customer2.age == get_feedback[1].age
        assert customer2.sex == get_feedback[1].sex
        assert customer2.first_visit == get_feedback[1].first_visit
        assert customer2.return_visit == get_feedback[1].return_visit
        assert customer2.clean == get_feedback[1].clean
        assert customer2.speed == get_feedback[1].speed
        assert customer2.food_quality == get_feedback[1].food_quality
        assert customer2.shisha == get_feedback[1].shisha
        assert customer2.comment == get_feedback[1].comment
        assert customer2.email == get_feedback[1].email

        # check customer 3 db entry
        assert customer3.name == get_feedback[2].name
        assert customer3.age == get_feedback[2].age
        assert customer3.sex == get_feedback[2].sex
        assert customer3.first_visit == get_feedback[2].first_visit
        assert customer3.return_visit == get_feedback[2].return_visit
        assert customer3.clean == get_feedback[2].clean
        assert customer3.speed == get_feedback[2].speed
        assert customer3.food_quality == get_feedback[2].food_quality
        assert customer3.shisha == get_feedback[2].shisha
        assert customer3.comment == get_feedback[2].comment
        assert customer3.email == get_feedback[2].email

    # remove db data
    session.delete(customer1_feedback)
    session.delete(customer2_feedback)
    session.delete(customer3_feedback)
    session.commit()

    with app.app_context():
        get_feedback: FeedbackForm = FeedbackForm.query.all()
        assert len(get_feedback) == 0

import pytest
from datetime import datetime
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.testing.client import client
from aurous79.models import FeedbackForm
from aurous79.utils.create_feedback import create_feedback


def test_get_hello_world():
    hello = "hello world"
    assert hello == "hello world"


def test_create_feedback(client):
    """Create new feedback form and check if exist in db"""
    # create feedback object
    feedback: FeedbackForm = FeedbackForm(
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
    # create db
    with app.app_context():
        session: SessionLocal = SessionLocal()
        new_feedback: FeedbackForm = FeedbackForm(
            name=feedback.name,
            age=feedback.age,
            sex=feedback.sex,
            first_visit=feedback.first_visit,
            return_visit=feedback.return_visit,
            clean=feedback.clean,
            service=feedback.service,
            speed=feedback.speed,
            food_quality=feedback.food_quality,
            shisha=feedback.shisha,
            comment=feedback.comment,
            email=feedback.email,
            timestamp=feedback.timestamp,
        )
        session.add(new_feedback)
        session.commit()

        # get data from db
        feedback_forms: FeedbackForm = FeedbackForm.query.all()

        # check if feedback object matches db data
        assert feedback.name == feedback_forms[0].name
        assert feedback.age == feedback_forms[0].age
        assert feedback.sex == feedback_forms[0].sex
        assert feedback.first_visit == feedback_forms[0].first_visit
        assert feedback.return_visit == feedback_forms[0].return_visit
        assert feedback.clean == feedback_forms[0].clean
        assert feedback.service == feedback_forms[0].service
        assert feedback.speed == feedback_forms[0].speed
        assert feedback.food_quality == feedback_forms[0].food_quality
        assert feedback.shisha == feedback_forms[0].shisha
        assert feedback.comment == feedback_forms[0].comment
        assert feedback.email == feedback_forms[0].email

        # check if only 1 entry created in db
        assert len(feedback_forms) == 1

        # remove db entry
        session.delete(new_feedback)
        session.commit()

    # check db after removing entry
    with app.app_context():
        feedback_forms: FeedbackForm = FeedbackForm.query.first()
        assert feedback_forms == None


def test_create_feedback_function(client):
    """Test if feedback function creates a feedback form"""
    # create a feedback object
    session: SessionLocal = SessionLocal()
    feedback: FeedbackForm = FeedbackForm(
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
    # create a feedback form
    new_feedback: FeedbackForm = create_feedback(
        name=feedback.name,
        age=feedback.age,
        sex=feedback.sex,
        first_visit=feedback.first_visit,
        return_visit=feedback.return_visit,
        clean=feedback.clean,
        service=feedback.service,
        speed=feedback.speed,
        food_quality=feedback.food_quality,
        shisha=feedback.shisha,
        comment=feedback.comment,
        email=feedback.email,
    )
    with app.app_context():
        # get data
        get_feedback: FeedbackForm = FeedbackForm.query.first()

        # check feedback object vs db data
        assert feedback.name == get_feedback.name
        assert feedback.age == get_feedback.age
        assert feedback.sex == get_feedback.sex
        assert feedback.first_visit == get_feedback.first_visit
        assert feedback.return_visit == get_feedback.return_visit
        assert feedback.clean == get_feedback.clean
        assert feedback.service == get_feedback.service
        assert feedback.speed == get_feedback.speed
        assert feedback.food_quality == get_feedback.food_quality
        assert feedback.shisha == get_feedback.shisha
        assert feedback.comment == get_feedback.comment
        assert feedback.email == get_feedback.email

    # remove db data
    session.delete(new_feedback)
    session.commit()

    # check if data has been removed
    with app.app_context():
        get_feedback: FeedbackForm = FeedbackForm.query.first()
        assert get_feedback == None

import pytest
from typing import List
from datetime import datetime
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.testing.client import client
from aurous79.models import FeedbackForm
from aurous79.utils.create_feedback import create_feedback
from aurous79.utils.report_functions import get_male_report, get_first_visit_report, get_return_visit_report, get_shisha_report, get_female_report, get_all_reports


def test_get_male_report(client):
    session: SessionLocal = SessionLocal()
    # create feedback object
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
        shisha="yes",
        comment="Male comment",
        email="john@email.com",
        timestamp=datetime.now(),
    )
    # add feedback object to db
    customer_feedback: FeedbackForm = create_feedback(
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
        email=customer.email
    )
    with app.app_context():
        # get feedback object from db
        get_feedback: FeedbackForm = FeedbackForm.query.first()
        # check if db object is same as feedback object
        assert customer.sex == get_feedback.sex
        assert customer.first_visit == get_feedback.first_visit
        assert customer.return_visit == get_feedback.return_visit
        assert customer.shisha == get_feedback.shisha
        
        # check male results
        male_result: FeedbackForm = get_male_report()
        assert male_result[0].sex == "male"
        assert male_result[0].sex == get_feedback.sex
        assert all(entry.sex == "male" for entry in male_result)

        # check first_visit results
        first_visit_results: FeedbackForm = get_first_visit_report()
        assert first_visit_results[0].first_visit == "yes"
        assert first_visit_results[0].first_visit == get_feedback.first_visit
        assert all(data.first_visit == "yes" for data in first_visit_results)

        # check return_visit results
        return_visit_results: FeedbackForm = get_return_visit_report()
        assert return_visit_results[0].return_visit == "yes"
        assert return_visit_results[0].return_visit == get_feedback.return_visit
        assert all(data.return_visit == "yes" for data in return_visit_results)

        # check get shisha results
        shisha_results: FeedbackForm = get_shisha_report()
        assert shisha_results[0].shisha == "yes"
        assert shisha_results[0].shisha == get_feedback.shisha
        assert all(data.shisha == "yes" for data in shisha_results)
    
    # remove db data
    session.delete(customer_feedback)
    session.commit()

    
    # check if data has been removed
    with app.app_context():
        get_feedback: FeedbackForm = FeedbackForm.query.first()
        assert get_feedback == None
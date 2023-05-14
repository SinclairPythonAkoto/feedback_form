import pytest
from typing import List, Tuple
from datetime import datetime
from random import randint
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.testing.client import client
from aurous79.models import FeedbackForm
from aurous79.utils.create_feedback import create_feedback
from aurous79.utils.graph_functions import (
    male_x,
    male_y,
    female_x,
    female_y,
    first_visit_x,
    first_visit_y,
    return_visit_x,
    return_visit_y,
    shisha_x,
    shisha_y,
    clean_x,
    clean_y,
    speed_x,
    speed_y,
    service_x,
    service_y,
)

male_results: List[Tuple] = [
    (
        "John Doe",
        17,
        "male",
        "yes",
        "yes",
        randint(1, 5),
        randint(1, 5),
        randint(1, 5),
        randint(1, 5),
        "yes",
        "Male comment",
        "john@email.com",
        datetime.now(),
    ),
    (
        "Max Jones",
        19,
        "male",
        "yes",
        "yes",
        randint(1, 5),
        randint(1, 5),
        randint(1, 5),
        randint(1, 5),
        "yes",
        "Male comment",
        "max@email.com",
        datetime.now(),
    ),
]

female_results: List[Tuple] = [
    (
        "Jane Doe",
        25,
        "female",
        "yes",
        "yes",
        randint(1, 5),
        randint(1, 5),
        randint(1, 5),
        randint(1, 5),
        "yes",
        "Female comment",
        "jane@email.com",
        datetime.now(),
    ),
    (
        "Mary Jane",
        35,
        "female",
        "yes",
        "yes",
        randint(1, 5),
        randint(1, 5),
        randint(1, 5),
        randint(1, 5),
        "yes",
        "Female comment",
        "mary@email.com",
        datetime.now(),
    ),
]


@pytest.mark.parametrize(
    "name,age,sex,first_visit,return_visit,clean,service,speed,food_quality,shisha,comment,email,timestamp",
    male_results,
)
def test_male_axis(
    name,
    age,
    sex,
    first_visit,
    return_visit,
    clean,
    service,
    speed,
    food_quality,
    shisha,
    comment,
    email,
    timestamp,
):
    """Test to find all male entries from db using male_x & male_y functions"""
    session: SessionLocal = SessionLocal()
    # create feedback object
    customer: FeedbackForm = FeedbackForm(
        name=name,
        age=age,
        sex=sex,
        first_visit=first_visit,
        return_visit=return_visit,
        clean=clean,
        service=service,
        speed=speed,
        food_quality=food_quality,
        shisha=shisha,
        comment=comment,
        email=email,
        timestamp=timestamp,
    )
    # store feedback object to db
    customer_feedback_1: FeedbackForm = create_feedback(
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
    customer_feedback_2: FeedbackForm = create_feedback(
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
    with app.app_context():
        # get 1st feedback object from db
        get_1_feedback: FeedbackForm = FeedbackForm.query.first()
        # check if db object is the same as feedback object
        assert get_1_feedback.sex == "male"
        assert customer.sex == get_1_feedback.sex
        # check if num of males macth X & Y axis function
        get_all_feedback: List[FeedbackForm] = FeedbackForm.query.all()
        assert all(data.sex == sex for data in get_all_feedback)

        assert male_x() == 2
        assert male_x() == len(get_all_feedback)

        assert male_y() == 2
        assert male_y() == len(get_all_feedback)

    session.delete(customer_feedback_1)
    session.delete(customer_feedback_2)
    session.commit()

    with app.app_context():
        get_1_feedback: FeedbackForm = FeedbackForm.query.first()
        assert get_1_feedback == None


@pytest.mark.parametrize(
    "name,age,sex,first_visit,return_visit,clean,service,speed,food_quality,shisha,comment,email,timestamp",
    female_results,
)
def test_female_axis(
    name,
    age,
    sex,
    first_visit,
    return_visit,
    clean,
    service,
    speed,
    food_quality,
    shisha,
    comment,
    email,
    timestamp,
):
    """Test to find all female entries from db using female_x & female_y functions"""
    session: SessionLocal = SessionLocal()
    # create feedback object
    customer: FeedbackForm = FeedbackForm(
        name=name,
        age=age,
        sex=sex,
        first_visit=first_visit,
        return_visit=return_visit,
        clean=clean,
        service=service,
        speed=speed,
        food_quality=food_quality,
        shisha=shisha,
        comment=comment,
        email=email,
        timestamp=timestamp,
    )
    # store feedback object to db
    customer_feedback_1: FeedbackForm = create_feedback(
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
    customer_feedback_2: FeedbackForm = create_feedback(
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
    with app.app_context():
        # get 1st feedback object from db
        get_1_feedback: FeedbackForm = FeedbackForm.query.first()
        # check if db object is the same as feedback object
        assert get_1_feedback.sex == "female"
        assert customer.sex == get_1_feedback.sex
        # check if num of females macth X & Y axis function
        get_all_feedback: List[FeedbackForm] = FeedbackForm.query.all()
        assert all(data.sex == sex for data in get_all_feedback)

        assert female_x() == 2
        assert female_x() == len(get_all_feedback)

        assert female_y() == 2
        assert female_y() == len(get_all_feedback)

    session.delete(customer_feedback_1)
    session.delete(customer_feedback_2)
    session.commit()

    with app.app_context():
        get_1_feedback: FeedbackForm = FeedbackForm.query.first()
        assert get_1_feedback == None


@pytest.mark.parametrize(
    "name,age,sex,first_visit,return_visit,clean,service,speed,food_quality,shisha,comment,email,timestamp",
    male_results,
)
def test_first_visit_axis(
    name,
    age,
    sex,
    first_visit,
    return_visit,
    clean,
    service,
    speed,
    food_quality,
    shisha,
    comment,
    email,
    timestamp,
):
    """Test to find all first_visit entries from db using X & Y functions"""
    session: SessionLocal = SessionLocal()
    # create feedback object
    customer: FeedbackForm = FeedbackForm(
        name=name,
        age=age,
        sex=sex,
        first_visit=first_visit,
        return_visit=return_visit,
        clean=clean,
        service=service,
        speed=speed,
        food_quality=food_quality,
        shisha=shisha,
        comment=comment,
        email=email,
        timestamp=timestamp,
    )
    # store feedback object to db
    customer_feedback_1: FeedbackForm = create_feedback(
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
    customer_feedback_2: FeedbackForm = create_feedback(
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
    with app.app_context():
        # get 1st feedback object from db
        get_1_feedback: FeedbackForm = FeedbackForm.query.first()
        # check if db object is the same as feedback object
        assert get_1_feedback.first_visit == "yes"
        assert customer.first_visit == get_1_feedback.first_visit
        # check if num of first_visit macth X & Y axis function
        get_all_feedback: List[FeedbackForm] = FeedbackForm.query.all()
        assert all(data.first_visit == first_visit for data in get_all_feedback)

        assert first_visit_x() == 2
        assert first_visit_x() == len(get_all_feedback)

        assert first_visit_y() == 2
        assert first_visit_y() == len(get_all_feedback)

    session.delete(customer_feedback_1)
    session.delete(customer_feedback_2)
    session.commit()

    with app.app_context():
        get_1_feedback: FeedbackForm = FeedbackForm.query.first()
        assert get_1_feedback == None


@pytest.mark.parametrize(
    "name,age,sex,first_visit,return_visit,clean,service,speed,food_quality,shisha,comment,email,timestamp",
    female_results,
)
def test_return_visit_axis(
    name,
    age,
    sex,
    first_visit,
    return_visit,
    clean,
    service,
    speed,
    food_quality,
    shisha,
    comment,
    email,
    timestamp,
):
    """Test to find all return_visit entries from db using X & Y functions"""
    session: SessionLocal = SessionLocal()
    # create feedback object
    customer: FeedbackForm = FeedbackForm(
        name=name,
        age=age,
        sex=sex,
        first_visit=first_visit,
        return_visit=return_visit,
        clean=clean,
        service=service,
        speed=speed,
        food_quality=food_quality,
        shisha=shisha,
        comment=comment,
        email=email,
        timestamp=timestamp,
    )
    # store feedback object to db
    customer_feedback_1: FeedbackForm = create_feedback(
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
    customer_feedback_2: FeedbackForm = create_feedback(
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
    with app.app_context():
        # get 1st feedback object from db
        get_1_feedback: FeedbackForm = FeedbackForm.query.first()
        # check if db object is the same as feedback object
        assert get_1_feedback.return_visit == "yes"
        assert customer.return_visit == get_1_feedback.return_visit
        # check if num of return_visit macth X & Y axis function
        get_all_feedback: List[FeedbackForm] = FeedbackForm.query.all()
        assert all(data.return_visit == return_visit for data in get_all_feedback)

        assert return_visit_x() == 2
        assert return_visit_x() == len(get_all_feedback)

        assert return_visit_y() == 2
        assert return_visit_y() == len(get_all_feedback)

    session.delete(customer_feedback_1)
    session.delete(customer_feedback_2)
    session.commit()

    with app.app_context():
        get_1_feedback: FeedbackForm = FeedbackForm.query.first()
        assert get_1_feedback == None


@pytest.mark.parametrize(
    "name,age,sex,first_visit,return_visit,clean,service,speed,food_quality,shisha,comment,email,timestamp",
    male_results,
)
def test_shisha_axis(
    name,
    age,
    sex,
    first_visit,
    return_visit,
    clean,
    service,
    speed,
    food_quality,
    shisha,
    comment,
    email,
    timestamp,
):
    """Test to find all shisha entries from db using X & Y functions"""
    session: SessionLocal = SessionLocal()
    # create feedback object
    customer: FeedbackForm = FeedbackForm(
        name=name,
        age=age,
        sex=sex,
        first_visit=first_visit,
        return_visit=return_visit,
        clean=clean,
        service=service,
        speed=speed,
        food_quality=food_quality,
        shisha=shisha,
        comment=comment,
        email=email,
        timestamp=timestamp,
    )
    # store feedback object to db
    customer_feedback_1: FeedbackForm = create_feedback(
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
    customer_feedback_2: FeedbackForm = create_feedback(
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
    with app.app_context():
        # get 1st feedback object from db
        get_1_feedback: FeedbackForm = FeedbackForm.query.first()
        # check if db object is the same as feedback object
        assert get_1_feedback.shisha == "yes"
        assert customer.shisha == get_1_feedback.shisha
        # check if num of shisha macth X & Y axis function
        get_all_feedback: List[FeedbackForm] = FeedbackForm.query.all()
        assert all(data.shisha == shisha for data in get_all_feedback)

        assert shisha_x() == 2
        assert shisha_x() == len(get_all_feedback)
        # check if shisha score 1 - 5
        # assert shisha_x() <= 5

        assert shisha_y() == 2
        assert shisha_y() == len(get_all_feedback)
        # check if shisha score 1 - 5
        # assert shisha_y() <= 5

    session.delete(customer_feedback_1)
    session.delete(customer_feedback_2)
    session.commit()

    with app.app_context():
        get_1_feedback: FeedbackForm = FeedbackForm.query.first()
        assert get_1_feedback == None

expected_results: List[Tuple] = [
    ("John Doe", 17, "male", "yes", "yes", 4, 5, 3, 4, "yes", "Comment from John", "john@email.com", datetime.now()),
    ("Jane Doe", 18, "female", "yes", "yes", 5, 3, 4, 4, "yes", "Comment from Jane", "jane@email.com", datetime.now()),
    ("Max Jones", 19, "male", "yes", "yes", 3, 4, 5, 4, "yes", "Comment from Max", "max@email.com", datetime.now()),
]


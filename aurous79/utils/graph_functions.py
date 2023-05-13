from typing import List
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.models import FeedbackForm
from aurous79.utils.report_functions import get_male_report, get_female_report, get_first_visit_report, get_return_visit_report, get_shisha_report

session: SessionLocal = SessionLocal()


# build X axis points
def male_x() -> int:
    """Finds all male entries from db to build X axis."""
    males: List[FeedbackForm] = get_male_report()
    value: int = len([val.sex for val in males])
    return value

def female_x() -> int:
    """Finds all female entries from db to build X axis."""
    females: List[FeedbackForm] = get_female_report()
    value: int = len([val.sex for val in females])
    return value


def first_visit_x() -> int:
    """Finds all first_visit entries from db to build X axis."""
    first_visitors: List[FeedbackForm] = get_first_visit_report()
    value: int = len([val.first_visit for val in first_visitors])
    return value


def return_visit_x() -> int:
    """Finds all return_visit entries from db to build X axis."""
    return_visitors: List[FeedbackForm] = get_return_visit_report()
    value: int = len([val.return_visit for val in return_visitors])
    return value


def shisha_x() -> int:
    """Finds all shisha entries from db to build X axis."""
    shisha: List[FeedbackForm] = get_shisha_report()
    value: int = len([val.shisha for val in shisha])
    return value

def clean_x() -> int:
    """Finds all clean entries from db to build X axis."""
    session: SessionLocal = SessionLocal()
    clean: List[FeedbackForm] = session.query(FeedbackForm.clean).all()
    value: List[int] = list(range(len([val.clean for val in clean])))
    return value[-1]

def service_x() -> int:
    """Finds all service entries from db to build X axis"""
    session: SessionLocal = SessionLocal()
    service: List[FeedbackForm] = session.query(FeedbackForm.service).all()
    value: List[int] = list(range(len([val.service for val in service])))
    return value[-1]

def speed_x() -> int:
    """Finds all speed entried from db to build X axis."""
    session: SessionLocal = SessionLocal()
    speed: List[FeedbackForm] = session.query(FeedbackForm.speed).all()
    value: List[int] = list(range(len([val.speed for val in speed])))
    return value[-1]

# build Y axis points
def male_y() -> int:
    """Finds all male entries from db to build Y axis."""
    males: List[FeedbackForm] = get_male_report()
    value: int = len([val.sex for val in males])
    return value

def female_y() -> int:
    """Finds all female entries from db to build Y axis."""
    females: List[FeedbackForm] = get_female_report()
    value: int = len([val.sex for val in females])
    return value


def first_visit_y() -> int:
    """Finds all first_visit entries from db to build Y axis."""
    first_visitors: List[FeedbackForm] = get_first_visit_report()
    value: int = len([val.first_visit for val in first_visitors])
    return value


def return_visit_y() -> int:
    """Finds all return_visit entries from db to build Y axis."""
    return_visitors: List[FeedbackForm] = get_return_visit_report()
    value: int = len([val.return_visit for val in return_visitors])
    return value


def shisha_y() -> int:
    """Finds all shisha entries from db to build Y axis."""
    shisha: List[FeedbackForm] = get_shisha_report()
    value: int = len([val.shisha for val in shisha])
    return value

def clean_y() -> int:
    """Finds all clean entries from db to build Y axis.

    Adds all entries, then divides by number of entries.
    """
    session: SessionLocal = SessionLocal()
    clean: List[FeedbackForm] = session.query(FeedbackForm.clean).all()
    sum_clean: int = sum([val.clean for val in clean])
    len_clean: len([val.clean for val in clean])
    return int(sum_clean / len_clean)

def service_y() -> int:
    """Finds all service entries from db to build Y axis.
    
    Adds all entries, then divides by number of entries.
    """
    session: SessionLocal = SessionLocal()
    service: List[FeedbackForm] = session.query(FeedbackForm.service).all()
    sum_service: int = sum([val.service for val in service])
    len_service: int = len([val.service for val in service])
    return int(sum_service / len_service)

def speed_y() -> int:
    """Finds all speed entries from db to build Y axis.
    
    Adds all entries, then divides by number of entries.
    """
    session: SessionLocal = SessionLocal()
    speed: List[FeedbackForm] = session.query(FeedbackForm.speed).all()
    sum_speed: int = sum([val.speed for val in speed])
    len_speed: int = len([val.speed for val in speed])
    return int(sum_speed / len_speed)
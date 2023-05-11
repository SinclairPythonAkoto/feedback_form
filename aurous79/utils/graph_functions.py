from typing import List
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.models import FeedbackForm, EmailLibrary
from aurous79.utils.report_functions import get_male_report, get_female_report, get_first_visit_report, get_return_visit_report, get_shisha_report

session: SessionLocal = SessionLocal()


# build X axis points
def male_x() -> int:
    """Finds all male entries from db to build X axis."""
    males: List[FeedbackForm] = get_male_report()
    value: int = len(val.sex for val in males)
    return value

def female_x() -> int:
    """Finds all female entries from db to build X axis."""
    females: List[FeedbackForm] = get_female_report()
    value: int = len(val.sex for val in females)
    return value


def first_visit_x() -> int:
    """Finds all first_visit entries from db to build X axis."""
    first_visitors: List[FeedbackForm] = get_first_visit_report()
    value: int = len(val.first_visit for val in first_visitors)
    return value


def return_visit_x() -> int:
    """Finds all return_visit entries from db to build X axis."""
    return_visitors: List[FeedbackForm] = get_return_visit_report()
    value: int = len(val.return_visit for val in return_visitors)
    return value


def shisha_x() -> int:
    """Finds all shisha entries from db to build X axis."""
    shisha: List[FeedbackForm] = get_shisha_report()
    value: int = len(val.shisha for val in shisha)
    return value

# build Y axis points
def male_y() -> int:
    """Finds all male entries from db to build Y axis."""
    males: List[FeedbackForm] = get_male_report()
    value: int = len(val.sex for val in males)
    return value

def female_y() -> int:
    """Finds all female entries from db to build Y axis."""
    females: List[FeedbackForm] = get_female_report()
    value: int = len(val.sex for val in females)
    return value


def first_visit_y() -> int:
    """Finds all first_visit entries from db to build Y axis."""
    first_visitors: List[FeedbackForm] = get_first_visit_report()
    value: int = len(val.first_visit for val in first_visitors)
    return value


def return_visit_y() -> int:
    """Finds all return_visit entries from db to build Y axis."""
    return_visitors: List[FeedbackForm] = get_return_visit_report()
    value: int = len(val.return_visit for val in return_visitors)
    return value


def shisha_y() -> int:
    """Finds all shisha entries from db to build Y axis."""
    shisha: List[FeedbackForm] = get_shisha_report()
    value: int = len(val.shisha for val in shisha)
    return value
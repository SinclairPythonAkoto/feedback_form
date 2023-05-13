from typing import List
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.models import FeedbackForm


def get_male_report() -> List[FeedbackForm]:
    """Get all male entries"""
    session: SessionLocal = SessionLocal()
    get_data: List[FeedbackForm] = (
        session.query(FeedbackForm).filter(FeedbackForm.sex == "male").all()
    )
    return get_data


def get_female_report() -> List[FeedbackForm]:
    """Get all female entries"""
    session: SessionLocal = SessionLocal()
    get_data: List[FeedbackForm] = (
        session.query(FeedbackForm).filter(FeedbackForm.sex == "female").all()
    )
    return get_data


def get_first_visit_report() -> List[FeedbackForm]:
    """Get first visit reports"""
    session: SessionLocal = SessionLocal()
    get_data: List[FeedbackForm] = (
        session.query(FeedbackForm).filter(FeedbackForm.first_visit == "yes").all()
    )
    return get_data


def get_return_visit_report() -> List[FeedbackForm]:
    """Get return visit reports"""
    session: SessionLocal = SessionLocal()
    get_data: List[FeedbackForm] = (
        session.query(FeedbackForm).filter(FeedbackForm.return_visit == "yes").all()
    )
    return get_data


def get_shisha_report() -> List[FeedbackForm]:
    """Get shisha reports"""
    session: SessionLocal = SessionLocal()
    get_data: List[FeedbackForm] = (
        session.query(FeedbackForm).filter(FeedbackForm.shisha == "yes").all()
    )
    return get_data


def get_all_reports() -> List[FeedbackForm]:
    """Get report on all data"""
    session: SessionLocal = SessionLocal()
    get_data: List[FeedbackForm] = (
        session.query(FeedbackForm).order_by(FeedbackForm.id).all()
    )
    return get_data

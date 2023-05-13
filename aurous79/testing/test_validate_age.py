import pytest
from aurous79.utils.validate_age import minimum_age, check_age


def test_validate_minimum_age():
    """Check if min age is 16+"""
    assert minimum_age(13) == False
    assert minimum_age(14) == False
    assert minimum_age(15) == False
    assert minimum_age(16) == True
    assert minimum_age(18) == True
    assert minimum_age(21) == True


def test_check_age():
    """Check if age 18+"""
    assert check_age(15) == False
    assert check_age(16) == False
    assert check_age(17) == False
    assert check_age(18) == True
    assert check_age(21) == True
    assert check_age(35) == True

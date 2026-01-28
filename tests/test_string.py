import pytest
from services.strings_utils import count_char, is_empty,is_valid_email,has_min_length


def test_valid_mail():
    assert is_valid_email('osg@hh.com')

def test_count_char():
    assert count_char('aderesg',"a")

def test_is_empty():
    assert is_empty(" ")

def test_has_min_length():
    assert has_min_length('helo',3)
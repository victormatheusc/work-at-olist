from jsonschema import validate, FormatChecker
from . import SCHEMA

def call_data_validator(data):
    try:
        validate(data, SCHEMA, format_checker=FormatChecker())
        return True
    except:
        return False

def date_validator(start_date, end_date):
    if end_date >= start_date:
        return True
    return False


def phone_validator(source, destination):
    if source != destination:
        return True
    return False

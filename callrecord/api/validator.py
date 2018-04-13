from jsonschema import validate, FormatChecker
from . import SCHEMA

def call_data_validator(data):
    try:
        validate(data, SCHEMA, format_checker=FormatChecker())
        return True
    except:
        return False

import re

from django.core.exceptions import ValidationError

REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PASSWORD = '^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,}$'

def password_validation(password):
    if not re.match(REGEX_PASSWORD, password):
        raise ValidationError('INVALID_PASSWORD')

def email_validation(email):
    if not re.match(REGEX_EMAIL, email):
        raise ValidationError('INVALID_EMAIL_ADDRESS')
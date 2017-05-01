import json


class ValidationError(BaseException):
    msg = None

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return 'Validation error: {}'.format(self.msg)


class NestedValidationError(Exception):
    errors = None

    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return json.dumps(self.errors)

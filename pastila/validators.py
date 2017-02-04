from pastila.exceptions import ValidationError


class Validator:
    def __call__(self, value, schema):
        return NotImplemented


class NumberRange(Validator):
    max = None
    min = None

    def __init__(self, max=None, min=None):
        self.max = max
        self.min = min

    def __call__(self, value, schema):
        if self.max is not None and value > self.max:
            raise ValidationError('must be less than {}'.format(self.max))

        if self.min is not None and value < self.min:
            raise ValidationError('must be greather than {}'.format(self.min))

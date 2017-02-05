from pastila.exceptions import ValidationError


class Field(object):
    _validators = []

    def __init__(self, validators=None):
        if validators is not None:
            self._validators = validators

    def dump(self, value):
        return NotImplemented

    def load(self, value):
        return NotImplemented

    def validate(self, value, schema):
        for validator in self._validators:
            validator(value, schema)


class StringField(Field):
    def dump(self, value):
        return value

    def load(self, value):
        return value


class IntegerField(Field):
    def dump(self, value):
        return value

    def load(self, value):
        try:
            return int(value)
        except ValueError:
            raise ValidationError('not valid integer')


class ListField(Field):
    base_field = None

    def __init__(self, base_field, *args, **kwargs):
        self.base_field = base_field
        super(ListField, self).__init__(*args, **kwargs)

    def load(self, value):
        return [self.base_field.load(item) for item in value]

    def dump(self, value):
        return [self.base_field.dump(item) for item in value]

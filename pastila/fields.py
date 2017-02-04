from pastila.exceptions import ValidationError


class BaseField:
    value = None
    _validators = []

    def __init__(self, validators=None):
        if validators is not None:
            self._validators = validators

    def _dump(self):
        return NotImplemented

    def _load(self, value):
        return NotImplemented

    def __set__(self, obj, value):
        self._load(value)

    def __get__(self, obj, type):
        return self.value

    def __repr__(self):
        return self.value

    def _validate(self, schema):
        for validator in self._validators:
            validator(self.value, schema)


class StringField(BaseField):
    def _dump(self):
        return self.value

    def _load(self, value):
        self.value = value


class IntegerField(BaseField):

    def __int__(self):
        return self.value

    def _dump(self):
        return self.value

    def _load(self, value):
        try:
            self.value = int(value)
        except ValueError:
            raise ValidationError('not valid integer')

from pastila.exceptions import ValidationError
from copy import deepcopy


class Field:
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

    def clone(self):
        return deepcopy(self)


class StringField(Field):
    def _dump(self):
        return self.value

    def _load(self, value):
        self.value = value


class IntegerField(Field):
    def _dump(self):
        return self.value

    def _load(self, value):
        try:
            self.value = int(value)
        except ValueError:
            raise ValidationError('not valid integer')


class ListField(Field):
    base_field = None

    def __init__(self, base_field, *args, **kwargs):
        self.base_field = base_field
        super(ListField, self).__init__(*args, **kwargs)

    def _load(self, value):
        self.value = []
        for item in value:
            field = self.base_field.clone()
            field._load(item)
            self.value.append(field)

    def _dump(self):
        return [item._dump() for item in self.value]

from pastila.exceptions import (
    ValidationError,
    NestedValidationError
)
from pastila.fields import Field


class Schema(object):
    _data = None
    _errors = None

    @property
    def data(self):
        return self._data

    @property
    def errors(self):
        return self._errors

    @property
    def fields(self):
        return {
            name: field for name, field in
            filter(lambda x: isinstance(x[1], Field), self.__class__.__dict__.items())
        }

    def __init__(self):
        self._data = dict()
        self._errors = dict()

    def set_error(self, field, exc):
        if isinstance(exc, NestedValidationError):
            self._errors[field] = exc.errors
        else:
            self._errors.setdefault(field, [])
            self._errors[field].append(str(exc))

    def load(self, data):
        for field, value in data.items():
            self.load_to_field(field, value)

        self.validate()

    def load_to_field(self, field, value):
        if field not in self.fields:
            return None
        try:
            self._data[field] = self.fields[field].load(value)
        except (ValidationError, NestedValidationError) as exc:
            self.set_error(field, exc)

    def validate(self):
        for name, field in self.fields.items():
            field.validate(self._data.get(name), self)

    def dump(self):
        data = {}
        for name, field in self.fields.items():
            data[name] = field.dump()

        return data

    def __getattr__(self, item):
        return self._data[item]

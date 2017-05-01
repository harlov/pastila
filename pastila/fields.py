from pastila.exceptions import (
    ValidationError,
    NestedValidationError
)


class Field(object):
    _validators = []

    def __init__(self, validators=None):
        if validators is not None:
            self._validators.extend(validators)

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
        errors = {}
        res = []
        for ind, item in enumerate(value):
            try:
                res.append(self.base_field.load(item))
            except ValidationError as exc:
                errors.setdefault(str(ind), [])
                errors[str(ind)].append(str(exc))
            except NestedValidationError as exc:
                errors[str(ind)] = exc.errors
        if errors:
            raise NestedValidationError(errors=errors)
        return res

    def dump(self, value):
        return [self.base_field.dump(item) for item in value]


class NestedField(Field):
    schema_class = None

    def __init__(self, schema, validators=None):
        self.schema_class = schema
        super(NestedField, self).__init__(validators)

    def load(self, value):
        schema = self.schema_class()
        schema.load(value)
        if schema.errors:
            raise NestedValidationError(errors=schema.errors)

        return schema.data

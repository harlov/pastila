from pastila.fields import BaseField


class Schema:

    def load(self, data):
        for field, value in data.items():
            self.load_to_field(field, value)

        self.validate()

    def validate(self):
        for field in self.fields.values():
            field._validate(self)

    def dump(self):
        data = {}
        for name, field in self.fields.items():
            data[name] = field._dump()

        return data

    @property
    def fields(self):
        return {
            name: field for name, field in
            filter(lambda x: isinstance(x[1], BaseField), self.__class__.__dict__.items())
        }

    def load_to_field(self, field, value):
        if field not in self.fields:
            return None

        self.fields[field]._load(value)

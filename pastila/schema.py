from pastila.fields import Field


class Schema(object):
    data = None

    def __init__(self):
        self.data = {}

    def load(self, data):
        for field, value in data.items():
            self.load_to_field(field, value)

        self.validate()

    def validate(self):
        for name, field in self.fields.items():
            field.validate(self.data[name], self)

    def dump(self):
        data = {}
        for name, field in self.fields.items():
            data[name] = field.dump()

        return data

    def __getattr__(self, item):
        return self.data[item]

    @property
    def fields(self):
        return {
            name: field for name, field in
            filter(lambda x: isinstance(x[1], Field), self.__class__.__dict__.items())
        }

    def load_to_field(self, field, value):
        if field not in self.fields:
            return None

        self.data[field] = self.fields[field].load(value)

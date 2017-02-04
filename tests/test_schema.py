from pastila.schema import Schema
from pastila.fields import StringField, IntegerField


class TestSchema(Schema):
    name = StringField()
    val1 = IntegerField()
    val2 = IntegerField()


def test_schema_load():
    test = TestSchema()
    test.load({
        'name': 'Test schema',
        'val1': 100,
        'val2': 200
    })

    test.name = 'Test schema changed'

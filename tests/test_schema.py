from pastila.schema import Schema
from pastila.fields import StringField, IntegerField, ListField

import pytest


@pytest.fixture()
def TestSchema():
    class TestSchema(Schema):
        name = StringField()
        val1 = IntegerField()
        val2 = IntegerField()
        arr_str = ListField(base_field=StringField())
        arr_int = ListField(base_field=IntegerField())

    return TestSchema


def test_schema_load(TestSchema):
    test = TestSchema()
    test.load({
        'name': 'Test schema',
        'val1': '100',
        'val2': '200',
        'arr_str': ['a', 'b', 'c', 'd'],
        'arr_int': [1, 2, 3, 4, 5]
    })

    assert test.data == {
        'name': 'Test schema',
        'val1': 100,
        'val2': 200,
        'arr_str': ['a', 'b', 'c', 'd'],
        'arr_int': [1, 2, 3, 4, 5]
    }

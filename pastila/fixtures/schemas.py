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


@pytest.fixture()
def TestNestedSchema():
    from pastila.schema import Schema
    from pastila.fields import StringField, IntegerField, NestedField

    class IntPropsSchema(Schema):
        key = StringField()
        value = IntegerField()

    class TestSchema(Schema):
        name = StringField()
        props = NestedField(schema=IntPropsSchema)

    return TestSchema


@pytest.fixture()
def TestNestedListSchema():
    from pastila.schema import Schema
    from pastila.fields import StringField, IntegerField, ListField, NestedField

    class IntPropsSchema(Schema):
        key = StringField()
        value = IntegerField()

    class TestSchema(Schema):
        name = StringField()
        props = ListField(NestedField(schema=IntPropsSchema))

    return TestSchema

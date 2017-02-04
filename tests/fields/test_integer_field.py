import pytest


def test_integer_field_load():
    from pastila.fields import IntegerField
    test = IntegerField()

    test._load('5')
    assert test.value == 5


def test_integer_field_dump():
    from pastila.fields import IntegerField
    test = IntegerField()
    test.value = 5

    assert test._dump() == 5


def test_integer_field_load_invalid_number():
    from pastila.fields import IntegerField
    from pastila.exceptions import ValidationError
    test = IntegerField()

    with pytest.raises(ValidationError) as e:
        test._load('5ww')
    assert str(e.value) == 'not valid integer'
    assert test.value is None

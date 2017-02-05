import pytest


def test_integer_field_load():
    from pastila.fields import IntegerField
    test = IntegerField()
    assert test.load('5') == 5


def test_integer_field_dump():
    from pastila.fields import IntegerField
    test = IntegerField()
    assert test.dump(5) == 5


def test_integer_field_load_invalid_number():
    from pastila.fields import IntegerField
    from pastila.exceptions import ValidationError
    test = IntegerField()
    with pytest.raises(ValidationError) as e:
        test.load('abc')
    assert str(e.value) == 'not valid integer'

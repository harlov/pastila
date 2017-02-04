import pytest


@pytest.mark.parametrize('max, min, value, is_valid', (
    (10, 2, 11, False),
    (10, 2, 10, True),
    (10, 2, 2, True),
    (1, 1, 1, True),
    (10, 2, 1, False)
)
)
def test_number_range_validator(max, min, value, is_valid):
    from pastila.validators import NumberRange
    from pastila.exceptions import ValidationError

    try:
        NumberRange(max=max, min=min)(value, None)
    except ValidationError as e:
        if is_valid:
            pytest.fail('Excpected field is valid')
    else:
        if not is_valid:
            pytest.fail('Excpected field is invalid')

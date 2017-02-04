def test_string_field_load():
    from pastila.fields import StringField
    test = StringField()

    test._load('test')
    assert test.value == 'test'


def test_string_field_dump():
    from pastila.fields import StringField
    test = StringField()
    test.value = 'test'
    assert test.value == 'test'

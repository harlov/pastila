def test_string_field_load():
    from pastila.fields import StringField
    test = StringField()

    assert test.load('test') == 'test'


def test_string_field_dump():
    from pastila.fields import StringField
    test = StringField()
    assert test.dump('test') == 'test'

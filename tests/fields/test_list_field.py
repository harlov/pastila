def test_list_field_load():
    from pastila.fields import ListField, StringField
    test = ListField(base_field=StringField())

    assert test.load(['abc', 'dce', 'afd']) == ['abc', 'dce', 'afd']


def test_list_field_dump():
    from pastila.fields import ListField, StringField

    test = ListField(base_field=StringField())

    assert test.dump(['abc', 'dce', 'afd']) == ['abc', 'dce', 'afd']

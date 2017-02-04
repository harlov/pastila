def test_list_field_load():
    from pastila.fields import ListField, StringField

    test = ListField(base_field=StringField())
    test._load(['abc', 'dce', 'afd'])

    assert [x.value for x in test.value] == ['abc', 'dce', 'afd']


def test_list_field_dump():
    from pastila.fields import ListField, StringField

    test = ListField(base_field=StringField())

    test._load(['abc', 'dce', 'afd'])

    assert test._dump() == ['abc', 'dce', 'afd']

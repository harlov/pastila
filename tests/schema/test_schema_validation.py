def test_schema_validation(TestSchema):
    test = TestSchema()

    test.load({
        'name': 'Name',
        'val1': 'www',
        'val2': 10,
        'arr_str': ['a', 'b', 'c'],
        'arr_int': [1, 'dva', 3]
    })

    assert test.errors == {
        'val1': ['not valid integer'],
        'arr_int': {
            '1': ['not valid integer']
        }
    }


def test_nested_schema_validation(TestNestedSchema):
    test = TestNestedSchema()
    test.load({
        'name': 'Name',
        'props': {
            'key': 'speed',
            'value': 'w10'
        }
    })
    assert test.errors == {
        'props': {
            'value': ['not valid integer']
        }
    }


def test_nested_list_schema_validation(TestNestedListSchema):
    test = TestNestedListSchema()
    test.load({
        'name': 'Name',
        'props': [{
            'key': 'speed',
            'value': '10'
        }, {
            'key': 'ang',
            'value': '10rad'
        }]
    })
    assert test.errors == {
        'props': {
            '1': {
                'value': ['not valid integer']
            }
        }
    }

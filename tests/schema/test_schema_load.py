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

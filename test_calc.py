from calc import db_to_linear

def test_3db_is_about_double():
    assert abs(db_to_linear(3) - 1.995) < 0.01

def test_0db_is_one():
    assert db_to_linear(0) == 1

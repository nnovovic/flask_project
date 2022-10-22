from app.util.parse import parse_bool


def test_parse_bool_true():
    assert parse_bool('True') is True


def test_parse_bool_false():
    assert parse_bool('False') is False


def test_parse_bool_default():
    assert parse_bool('Something') is False

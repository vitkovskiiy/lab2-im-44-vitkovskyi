from calculator.core import parse


def test_parse_splits_keys_separated_by_single_space():
    assert parse("1 2 3 + 4 5 6 =") == ["1", "2", "3", "+", "4", "5", "6", "="]

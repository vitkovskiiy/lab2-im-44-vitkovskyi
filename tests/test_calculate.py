import pytest

from calculator.core import calculate

# Required examples from the assignment: key list => number on the screen.
REQUIRED_EXAMPLES = [
    ([], 0),
    (["5"], 5),
    (["1", "2"], 12),
    (["1", "2", "3", "+", "4", "5", "6", "="], 579),
    (["1", "2", "3", "-", "2", "3", "="], 100),
    (["1", "0", "-", "1", "0", "0", "="], -90),
    (["1", "0", "*", "2", "2", "="], 220),
    (["1", "0", "0", "/", "3", "="], 33),
    (["9", "/", "1", "0", "="], 0),
    (["1", "2", "3", "+"], 123),
    (["1", "2", "3", "+", "4"], 4),
    (["1", "2", "3", "+", "4", "5", "6"], 456),
]


@pytest.mark.parametrize("keys, expected", REQUIRED_EXAMPLES)
def test_calculate_returns_screen_after_last_key_for_required_examples(keys, expected):
    assert calculate(keys) == expected

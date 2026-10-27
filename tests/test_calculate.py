import pytest

from calculator.core import calculate, parse

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


# The same required examples as they appear in the input file.
REQUIRED_TEXT_EXAMPLES = [
    ("", 0),
    ("5", 5),
    ("1 2", 12),
    ("1 2 3 + 4 5 6 =", 579),
    ("1 2 3 - 2 3 =", 100),
    ("1 0 - 1 0 0 =", -90),
    ("1 0 * 2 2 =", 220),
    ("1 0 0 / 3 =", 33),
    ("9 / 1 0 =", 0),
    ("1 2 3 +", 123),
    ("1 2 3 + 4", 4),
    ("1 2 3 + 4 5 6", 456),
]


@pytest.mark.parametrize("text, expected", REQUIRED_TEXT_EXAMPLES)
def test_parse_then_calculate_returns_screen_for_required_examples(text, expected):
    assert calculate(parse(text)) == expected


def test_leading_zeros_are_dropped_from_screen():
    assert calculate(["0", "0", "5"]) == 5


def test_subtraction_of_larger_number_gives_negative_result():
    assert calculate(["3", "-", "5", "="]) == -2


def test_subtraction_of_equal_numbers_gives_zero():
    assert calculate(["7", "-", "7", "="]) == 0


def test_division_with_remainder_rounds_down():
    assert calculate(["7", "/", "2", "="]) == 3


def test_multiplication_by_zero_gives_zero():
    assert calculate(["1", "2", "*", "0", "="]) == 0


def test_large_operands_multiply_without_overflow():
    keys = ["9"] * 20 + ["*"] + ["9"] * 20 + ["="]

    assert calculate(keys) == 9999999999999999999800000000000000000001


def test_division_by_zero_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        calculate(["5", "/", "0", "="])


@pytest.mark.parametrize(
    "keys",
    [
        ["1", "2", "a"],
        ["5", "="],
        ["1", "+", "2", "*", "3"],
    ],
    ids=["unknown key", "equals without operator", "second operator"],
)
def test_calculate_raises_value_error_for_invalid_input(keys):
    with pytest.raises(ValueError):
        calculate(keys)

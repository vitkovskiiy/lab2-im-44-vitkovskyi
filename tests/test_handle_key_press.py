import pytest

from calculator.core import CalculatorState, handle_key_press


def test_digit_on_fresh_state_is_shown_on_screen():
    state = CalculatorState()

    handle_key_press(state, "5")

    assert state == CalculatorState(
        screen=5, first_number=0, op=None, start_second_number=False
    )


def test_plus_stores_operator_copies_screen_to_first_number_and_sets_flag():
    state = CalculatorState(screen=123)

    handle_key_press(state, "+")

    assert state == CalculatorState(
        screen=123, first_number=123, op="+", start_second_number=True
    )


@pytest.mark.parametrize("operator", ["-", "*", "/"])
def test_minus_multiply_divide_store_operator_copy_screen_and_set_flag(operator):
    state = CalculatorState(screen=123)

    handle_key_press(state, operator)

    assert state == CalculatorState(
        screen=123, first_number=123, op=operator, start_second_number=True
    )


def test_digit_after_operator_replaces_screen_and_clears_flag():
    state = CalculatorState(
        screen=123, first_number=123, op="+", start_second_number=True
    )

    handle_key_press(state, "4")

    assert state == CalculatorState(
        screen=4, first_number=123, op="+", start_second_number=False
    )


def test_equals_with_plus_shows_sum_of_first_number_and_screen():
    state = CalculatorState(
        screen=456, first_number=123, op="+", start_second_number=False
    )

    handle_key_press(state, "=")

    assert state == CalculatorState(
        screen=579, first_number=123, op="+", start_second_number=False
    )


def test_equals_with_minus_subtracts_screen_from_first_number():
    state = CalculatorState(
        screen=23, first_number=123, op="-", start_second_number=False
    )

    handle_key_press(state, "=")

    assert state == CalculatorState(
        screen=100, first_number=123, op="-", start_second_number=False
    )


def test_equals_with_multiply_shows_product_of_first_number_and_screen():
    state = CalculatorState(
        screen=22, first_number=10, op="*", start_second_number=False
    )

    handle_key_press(state, "=")

    assert state == CalculatorState(
        screen=220, first_number=10, op="*", start_second_number=False
    )


def test_equals_with_divide_shows_quotient_rounded_down():
    state = CalculatorState(
        screen=3, first_number=100, op="/", start_second_number=False
    )

    handle_key_press(state, "=")

    assert state == CalculatorState(
        screen=33, first_number=100, op="/", start_second_number=False
    )


@pytest.mark.parametrize("key", ["x", "%", "12", "-5", " 7"])
def test_unknown_key_raises_value_error(key):
    state = CalculatorState(screen=3)

    with pytest.raises(ValueError):
        handle_key_press(state, key)


def test_equals_without_operator_raises_value_error():
    state = CalculatorState(screen=5)

    with pytest.raises(ValueError):
        handle_key_press(state, "=")

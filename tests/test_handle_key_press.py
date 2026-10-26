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

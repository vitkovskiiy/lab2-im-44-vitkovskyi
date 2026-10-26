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

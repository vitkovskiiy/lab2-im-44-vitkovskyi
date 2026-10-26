from calculator.core import CalculatorState, handle_key_press


def test_digit_on_fresh_state_is_shown_on_screen():
    state = CalculatorState()

    handle_key_press(state, "5")

    assert state == CalculatorState(
        screen=5, first_number=0, op=None, start_second_number=False
    )

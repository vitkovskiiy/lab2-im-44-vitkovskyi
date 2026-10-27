from dataclasses import dataclass

DIGITS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


@dataclass
class CalculatorState:
    screen: int = 0
    first_number: int = 0
    op: str | None = None
    start_second_number: bool = False


def parse(text: str) -> list[str]:
    return text.split()


def handle_key_press(state: CalculatorState, key: str) -> None:
    if key in ("+", "-", "*", "/"):
        state.op = key
        state.start_second_number = True
        state.first_number = state.screen
    elif key == "=":
        if state.op == "-":
            state.screen = state.first_number - state.screen
        elif state.op == "*":
            state.screen = state.first_number * state.screen
        elif state.op == "/":
            state.screen = state.first_number // state.screen
        else:
            state.screen = state.first_number + state.screen
    elif key in DIGITS:
        if state.start_second_number:
            state.screen = int(key)
        else:
            state.screen = state.screen * 10 + int(key)
        state.start_second_number = False
    else:
        raise ValueError(f"unknown key: {key!r}")

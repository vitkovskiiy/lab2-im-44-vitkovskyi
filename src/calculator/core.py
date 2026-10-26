from dataclasses import dataclass


@dataclass
class CalculatorState:
    screen: int = 0
    first_number: int = 0
    op: str | None = None
    start_second_number: bool = False


def parse(text: str) -> list[str]:
    return text.split()


def handle_key_press(state: CalculatorState, key: str) -> None:
    if key == "+":
        state.op = key
        state.start_second_number = True
        state.first_number = state.screen
    else:
        state.screen = state.screen * 10 + int(key)

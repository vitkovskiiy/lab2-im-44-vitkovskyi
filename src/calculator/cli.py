import sys

from .core import calculate, parse


def main(argv: list[str] | None = None) -> None:
    input_path, output_path = sys.argv[1:] if argv is None else argv
    with open(input_path, encoding="utf-8") as f:
        text = f.read()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(calculate(parse(text))))

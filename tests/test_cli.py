from calculator.cli import main


def test_cli_writes_screen_value_from_input_file_to_output_file(tmp_path):
    input_path = tmp_path / "input.txt"
    output_path = tmp_path / "output.txt"
    input_path.write_text("1 2 3 + 4 5 6 =", encoding="utf-8")

    main([str(input_path), str(output_path)])

    assert output_path.read_text(encoding="utf-8") == "579"

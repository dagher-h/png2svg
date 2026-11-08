from png2svg.cli import build_parser, main


def test_parser_accepts_input_and_output():
    args = build_parser().parse_args(["input.png", "output.svg"])
    assert args.input == "input.png"
    assert args.output == "output.svg"


def test_parser_accepts_size_option():
    args = build_parser().parse_args(["in.png", "out.svg", "--size", "20"])
    assert args.size == 20


def test_main_creates_svg_file(tmp_path, monkeypatch):
    from PIL import Image

    input_path = tmp_path / "input.png"
    output_path = tmp_path / "output.svg"
    Image.new("RGB", (50, 50), (255, 0, 0)).save(input_path)

    monkeypatch.setattr("sys.argv", ["png2svg", str(input_path), str(output_path)])
    main()

    assert output_path.exists()
    content = output_path.read_text()
    assert content.startswith("<svg")

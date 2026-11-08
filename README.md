# png2svg

Convert a PNG image into a scalable hexagonal SVG wallpaper.

The tool reads a low-resolution PNG, samples its colors over a hexagonal grid, and produces a crisp, infinitely scalable SVG that can be used as a high-resolution wallpaper on any screen.

## How it works

1. The image is covered with a hexagonal grid.
2. For each hexagon, the average color of the underlying pixels is sampled.
3. Each hexagon is drawn as an SVG polygon filled with that color.
4. All hexagons are assembled into a single SVG document.

## Requirements

- Python 3.11+
- uv (https://docs.astral.sh/uv/)

## Installation

    uv sync

## Usage (command line)

    uv run png2svg input.png output.svg

Optional parameters:

    uv run png2svg input.png output.svg --size 15 --radius 4

- --size: hexagon size (default: 10). Larger means fewer, bigger hexagons.
- --radius: color sampling radius (default: 3).

## Usage (interactive notebook)

    uv run marimo edit notebooks/explorer.py

Pick a PNG file and adjust the hexagon size with a slider to see the result live.

## Development

Run the full quality suite:

    uv run ruff format .
    uv run ruff check .
    uv run mypy src
    uv run pytest --cov=src --cov-report=term-missing

Every push to main runs these checks automatically on Python 3.11, 3.12 and 3.13 via GitHub Actions.

## License

MIT
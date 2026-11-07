"""Command-line interface for png2svg."""

import argparse

from PIL import Image

from png2svg.core import image_to_svg


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="png2svg",
        description="Convert a PNG image into a scalable hexagonal SVG wallpaper.",
    )
    parser.add_argument("input", help="Path to the input PNG file.")
    parser.add_argument("output", help="Path to the output SVG file.")
    parser.add_argument("--size", type=int, default=10, help="Hexagon size (default: 10).")
    parser.add_argument("--radius", type=int, default=3, help="Color sampling radius (default: 3).")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    img = Image.open(args.input)
    svg = image_to_svg(img, size=args.size, radius=args.radius)
    with open(args.output, "w") as f:
        f.write(svg)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()

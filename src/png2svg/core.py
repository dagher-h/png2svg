import math

from PIL import Image


def hexagon_svg(cx: float, cy: float, size: float, color: tuple[int, int, int]) -> str:
    """Return the SVG <polygon> markup for a hexagon.

    cx, cy: center of the hexagon.
    size:   distance from the center to each vertex.
    color:  (r, g, b) fill color, each 0-255.
    """
    points = []
    for i in range(6):
        angle = math.pi / 3 * i  # 0, 60, 120, 180, 240, 300 degrees in radians
        x = cx + size * math.cos(angle)  # x coordinate of this vertex
        y = cy + size * math.sin(angle)  # y coordinate of this vertex
        points.append(f"{x:.1f},{y:.1f}")
    points_str = " ".join(points)
    r, g, b = color
    return f'<polygon points="{points_str}" fill="rgb({r},{g},{b})" />'


def sample_color(img: Image.Image, cx: int, cy: int, radius: int) -> tuple[int, int, int]:
    """Return the average (r, g, b) color around (cx, cy)."""
    rgb_img = img.convert("RGB")
    width, height = rgb_img.size
    reds, greens, blues = [], [], []
    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):
            x = cx + dx
            y = cy + dy
            if 0 <= x < width and 0 <= y < height:
                pixel = rgb_img.getpixel((x, y))
                r, g, b = pixel  # type: ignore[misc]
                reds.append(r)
                greens.append(g)
                blues.append(b)
    avg_r = sum(reds) // len(reds)
    avg_g = sum(greens) // len(greens)
    avg_b = sum(blues) // len(blues)
    return (avg_r, avg_g, avg_b)


def hexagon_centers(width: int, height: int, size: float) -> list[tuple[float, float]]:
    """Return the center points of all hexagons covering a width x height area."""
    centers = []
    horizontal_spacing = 1.5 * size
    vertical_spacing = math.sqrt(3) * size
    col = 0
    x = 0.0
    while x <= width:
        # odd columns are shifted down by half a row
        y_offset = vertical_spacing / 2 if col % 2 == 1 else 0.0
        y = y_offset
        while y <= height:
            centers.append((x, y))
            y += vertical_spacing
        x += horizontal_spacing
        col += 1
    return centers


def image_to_svg(img: Image.Image, size: float = 10, radius: int = 3) -> str:
    """Convert a Pillow image into a complete hexagonal SVG document.

    size:   distance from a hexagon center to its vertices.
    radius: how far around each center to sample the color.
    """
    rgb_img = img.convert("RGB")
    width, height = rgb_img.size

    hexagons = []
    for cx, cy in hexagon_centers(width, height, size):
        color = sample_color(rgb_img, int(cx), int(cy), radius)
        hexagons.append(hexagon_svg(cx, cy, size, color))

    body = "\n".join(hexagons)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">\n'
        f"{body}\n"
        f"</svg>"
    )

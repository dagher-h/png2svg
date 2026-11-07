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
import math


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

from PIL import Image

from png2svg.core import hexagon_svg, sample_color


def test_hexagon_svg_is_a_polygon():
    result = hexagon_svg(50, 50, 10, (255, 0, 0))
    assert result.startswith("<polygon")
    assert result.endswith("/>")


def test_hexagon_svg_has_the_fill_color():
    result = hexagon_svg(50, 50, 10, (255, 0, 0))
    assert 'fill="rgb(255,0,0)"' in result


def test_hexagon_svg_has_six_points():
    result = hexagon_svg(50, 50, 10, (255, 0, 0))
    start = result.index('points="') + len('points="')
    end = result.index('"', start)
    points = result[start:end].split()
    assert len(points) == 6


def test_sample_color_on_uniform_image():
    img = Image.new("RGB", (20, 20), (255, 0, 0))
    color = sample_color(img, 10, 10, 5)
    assert color == (255, 0, 0)


def test_sample_color_returns_three_ints():
    img = Image.new("RGB", (20, 20), (10, 20, 30))
    color = sample_color(img, 10, 10, 5)
    assert len(color) == 3
    assert all(isinstance(c, int) for c in color)

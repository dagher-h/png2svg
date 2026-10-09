from png2svg.core import hexagon_svg


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

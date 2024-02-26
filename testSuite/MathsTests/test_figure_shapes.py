from pytest import mark

from Code.Maths.Figure_shapes import Square, Circle, Triangle

params_square_area = [(4, 16)]
params_triangle_perimeter = [(3, 3, 3, 9)]


@mark.parametrize("side, area", params_square_area)
def test_square(side, area):
    obj = Square(side)

    assert obj.calculate_area == area


@mark.parametrize("side1, side2, side3, perimeter", params_triangle_perimeter)
def test_triangle_perimeter(side1, side2, side3, perimeter):
    obj = Triangle(side1, side2, side3)

    assert obj.calculate_perimeter == perimeter

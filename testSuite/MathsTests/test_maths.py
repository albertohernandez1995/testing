from pytest import mark

from Code.Maths.rectangles import Rectangle

params_surface = [
    (10, 5, 50),
    (10, 2, 20),
    (3, 5, 15),
    (8, 5, 40),
]

params_perimeter = [
    (5, 5, 20),
    (3, 6, 18),
    (9, 7, 32),
    (1, 1, 4)
]


@mark.parametrize("height, width, reference", params_surface)
def test_rectangle_surface(height, width, reference):
    obj = Rectangle(height, width)

    assert obj.surface == reference

@mark.parametrize("height, width, reference", params_perimeter)
def test_rectangle_perimeter(height, width, reference):
    obj = Rectangle(height, width)

    assert obj.perimeter == reference

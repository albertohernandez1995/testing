from pytest import mark

from Code.Maths.rectangles import Rectangle

params = [
    (10, 5, 50),
    (10, 2, 20),
    (3, 5, 15),
    (8, 5, 40),
]


@mark.parametrize("height, width, reference", params)
def test_rectangle_surface(height, width, reference):
    obj = Rectangle(height, width)

    assert obj.surface == reference

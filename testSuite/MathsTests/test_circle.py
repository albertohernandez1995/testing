from pytest import mark

from Code.Maths.Circle import Circle

params_area = [(3.14, 5, 78.5)]


@mark.parametrize("pi, radio, reference", params_area)
def test_circle_area(pi, radio, reference):
    obj = Circle(pi, radio)

    assert obj.circle_area == reference

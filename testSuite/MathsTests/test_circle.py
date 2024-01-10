from pytest import mark

from Code.Maths.Circle import Circle

params_area = [(5, 78.54), (2, 12.566)]

params_circunference = [(5, 31.416)]


@mark.parametrize("radio, reference", params_area)
def test_circle_area(radio, reference):
    obj = Circle(radio)

    assert obj.circle_area == reference


@mark.parametrize("radio, reference", params_circunference)
def test_circle_circunference(radio, reference):
    obj = Circle(radio)

    assert obj.circle_circunference == reference

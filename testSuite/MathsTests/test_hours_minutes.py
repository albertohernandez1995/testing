from pytest import mark
from Code.Maths.Hours_minutes import minutes_to_hours

params = [(90, "hours: 1 minutes: 30")]


@mark.parametrize("number, print", params)
def test_hours_to_minutes(number, horas_minutos):
    result = minutes_to_hours(number)

    assert result == horas_minutos

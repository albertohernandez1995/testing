from pytest import mark

from Code.People_Strings.Student import Student

params_datos = [("Alberto", 29, 5), ("Javier", 25, 10)]


@mark.parametrize("name, age, grade", params_datos)
def test_datos(name, age, grade):
    obj = Student(name, age, grade)

    assert obj

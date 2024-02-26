from pytest import fixture


@fixture
def input_path(request):
    base_path = request.node.get_closest_marker('input_path').args[0]
    return base_path


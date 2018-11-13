import pytest


def get_fixture_value(request, fixture_name):
    """
    Returns the value associated with fixture named `fixture_name`, in provided request context.
    This is just an easy way to use `getfixturevalue` or `getfuncargvalue` according to whichever is availabl in
    current pytest version

    :param request:
    :param fixture_name:
    :return:
    """
    try:
        # Pytest 4+ or latest 3.x (to avoid the deprecated warning)
        return request.getfixturevalue(fixture_name)
    except AttributeError:
        # Pytest 3-
        return request.getfuncargvalue(fixture_name)


# Create a symbol that will work to create a fixture containing 'yield', whatever the pytest version
if int(pytest.__version__.split('.', 1)[0]) < 3:
    yield_fixture = pytest.yield_fixture
else:
    yield_fixture = pytest.fixture

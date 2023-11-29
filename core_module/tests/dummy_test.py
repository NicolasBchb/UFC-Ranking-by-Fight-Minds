from fmranker.dummy import dummy_func


def test_dummy_func():
    assert dummy_func(2, 3) == 5

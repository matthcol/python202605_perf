from collections.abc import Iterator

from utils import skip


def test_skip_empty():
    it = skip([], 0)
    assert isinstance(it, Iterator)
    assert list(it) == []

def test_skip_over_the_limit():
    it = skip([1, 2, 3], 10)
    assert isinstance(it, Iterator)
    assert list(it) == []

def test_dummy():
    pass
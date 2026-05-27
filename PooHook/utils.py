

# TODO: improve typing


from typing import Iterable


def skip[E](iterable: Iterable[E], n: int) -> Iterable[E]:
    """Return an iterator on the iterable object which has advanced of n steps.

    Parameters:
    - n : number of elements to skip (must be positive or null)
    """
    assert n >= 0, "number of skipped values must be positive or null"
    it = iter(iterable)
    try:
        for _ in range(n):
            next(it)
    except StopIteration:
        pass
    return it

# TODO: function limit(iterable, n)

# tests manuels => tests auto
if __name__ == '__main__':
    print(list(skip([1, 2 , 3], 0)))
    print(list(skip([1, 2 , 3], 1)))
    print(list(skip([1, 2 , 3], 2)))
    print(list(skip([1, 2 , 3], 3)))
    print(list(skip([1, 2 , 3], 4)))
    # print(list(skip([1, 2 , 3], -1))) # print(list(skip([1, 2 , 3], -1)))
    # print(list(skip(123, 2))) # Linter error + dynamic error : TypeError: 'int' object is not iterable

    # typing 
    it = skip([1, 2 , 3], 0)

import itertools


def neighbors(point):
    dim = len(point)
    zero = tuple(0 for _ in point)
    for v in itertools.product((-1, 0, 1), repeat=dim):
        if v != zero:
            yield tuple(x + y for x, y in zip(point, v))

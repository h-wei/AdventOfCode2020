class Day15:
    @staticmethod
    def part1(starting, turn):
        d = [0] * turn
        n = len(starting)
        for i in range(n-1):
            d[starting[i]] = i+1
        last = starting[-1]
        for i in range(n, turn):
            j, d[last] = d[last], i
            last = i - j if j > 0 else 0
        return last

def test():
    print(Day15.part1((0,3,6), 10))
    for v, t, e in (
        ((1,3,2), 2020,1),
        ((2,1,3), 2020, 10),
        ((1,2,3), 2020, 27),
        ((2,3,1), 2020, 78),
        ((3,2,1), 2020, 438),
        ((3,1,2), 2020, 1836)
    ):
        assert Day15.part1(v, t) == e

def solve():
    print(Day15.part1((0,13,16,17,1,10,6), 2020))
    print(Day15.part1((0,13,16,17,1,10,6), 30000000))

test()
solve()

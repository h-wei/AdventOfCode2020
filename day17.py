from collections import defaultdict
import utils


class Day17:
    def __init__(self, content):
        self.lines = content.split("\n")
        self.y = len(self.lines)
        self.x = len(self.lines[0])

    def _get_active(self, dim):
        self.active = set()
        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                if c == "#":
                    self.active.add((x, y) + tuple(0 for _ in range(dim - 2)))

    def _one_run(self, i):
        active = set()
        neighbors = defaultdict(int)
        for point in self.active:
            for neighbor in utils.neighbors(point):
                neighbors[neighbor] += 1

        for neighbor in neighbors:
            if neighbor in self.active and neighbors[neighbor] in (2, 3):
                active.add(neighbor)
            elif neighbor not in self.active and neighbors[neighbor] == 3:
                active.add(neighbor)

        self.active = active

    def part1(self):
        self._get_active(3)
        for i in range(6):
            self._one_run(i)
        return len(self.active)

    def part2(self):
        self._get_active(4)
        for i in range(6):
            self._one_run(i)
        return len(self.active)


def test():
    content = """.#.
..#
###"""
    day17 = Day17(content)
    assert day17.part1() == 112
    assert day17.part2() == 848


def solve():
    content = open("input/17.txt").read()
    day17 = Day17(content)
    print(day17.part1())
    print(day17.part2())


test()
solve()

class Day12:
    def __init__(self, content):
        self.actions = [(line[0], int(line[1:])) for line in content.split("\n")]
        self.tokens = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

    def part1(self):
        directions = "ENWS"
        d, north, east = 0, 0, 0
        for a, v in self.actions:
            if a == "L":
                d = (d + v // 90) % 4
            elif a == "R":
                d = (d + 4 - v // 90) % 4
            elif a == "F":
                i, j = self.tokens[directions[d]]
                east += i * v
                north += j * v
            else:
                i, j = self.tokens[a]
                east += i * v
                north += j * v
        return abs(north) + abs(east)

    def part2(self):
        east, north = 10, 1
        x, y = 0, 0
        for a, v in self.actions:
            if a == "L":
                if v == 90:
                    east, north = -north, east
                elif v == 180:
                    east, north = -east, -north
                elif v == 270:
                    east, north = north, -east
            elif a == "R":
                if v == 90:
                    east, north = north, -east
                elif v == 180:
                    east, north = -east, -north
                elif v == 270:
                    east, north = -north, east
            elif a == "F":
                x += east * v
                y += north * v
            else:
                i, j = self.tokens[a]
                east += i * v
                north += j * v
        return abs(x) + abs(y)


def test():
    content = """F10
N3
F7
R90
F11"""
    day12 = Day12(content)
    assert day12.part1() == 25
    assert day12.part2() == 286


def solve():
    content = open("input/12.txt").read()
    day12 = Day12(content)
    print(day12.part1())
    print(day12.part2())


test()
solve()

class Day3:
    def __init__(self, content):
        self.grid = content.split("\n")

    def part1(self, right=3, down=1):
        count = j = 0
        m, n = len(self.grid), len(self.grid[0])
        for i in range(0, m, down):
            if self.grid[i][j % n] == "#":
                count += 1
            j += right
        return count

    def part2(self):
        product = 1
        for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
            product *= self.part1(right, down)
        return product


def test():
    content = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    day3 = Day3(content)
    assert day3.part1() == 7
    assert day3.part2() == 336


def solve():
    content = open("input/3.txt").read()
    day3 = Day3(content)
    print(day3.part1())
    print(day3.part2())


test()
solve()
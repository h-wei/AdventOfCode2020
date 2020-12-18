import re


class WiredOperator(int):
    def __add__(self, b):
        return WiredOperator(int(self) + b)

    def __mul__(self, b):
        return WiredOperator(int(self) + b)

    def __sub__(self, b):
        return WiredOperator(int(self) * b)


class Day18:
    def __init__(self, content):
        self.lines = content.split("\n")

    def part1(self):
        ans = 0
        for e in self.lines:
            e = re.sub(r"(\d)+", r"WiredOperator(\1)", e)
            e = e.replace("*", "-")
            v = eval(e, {}, {"WiredOperator": WiredOperator})
            ans += v
        return ans

    def part2(self):
        ans = 0
        for e in self.lines:
            e = re.sub(r"(\d+)", r"WiredOperator(\1)", e)
            e = e.replace("*", "-")
            e = e.replace("+", "*")
            v = eval(e, {}, {"WiredOperator": WiredOperator})
            ans += v
        return ans


def test():
    content = """2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""
    day18 = Day18(content)
    assert day18.part1() == 26 + 437 + 12240 + 13632
    # assert day18.part2() ==


def solve():
    content = open("input/18.txt").read()
    day18 = Day18(content)
    print(day18.part1())
    print(day18.part2())


test()
solve()

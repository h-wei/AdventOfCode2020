#! /usr/bin/env python3

import sys


def generate(day):
    with open(f"day{day}.py", "w") as f:
        f.write(
            f'''class Day{day}:
    def __init__(self, content):

    def part1(self):
        return None

    def part2(self):
        return None

def test():
    content = """"""
    day{day} = Day{day}(content)
    assert day{day}.part1() ==
    assert day{day}.part2() ==

def solve():
    content = open('input/{day}.txt').read()
    day{day} = Day{day}(content)
    print(day{day}.part1())
    print(day{day}.part2())

test()
solve()
'''
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python3 day.py day")
        sys.exit(1)
    day = sys.argv[1]
    generate(day)

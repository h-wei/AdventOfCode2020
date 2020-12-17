from collections import deque


class Day7:
    def __init__(self, content):
        self._parse(content)

    def _parse(self, content):
        self.items = {}
        for line in content.split("\n"):
            bags = line.split(" contain ")
            parent = bags[0][:-5]
            if "no" in bags[1]:
                self.items[parent] = {}
            else:
                temp = {}
                for kid in bags[1][:-1].split(", "):
                    offset = kid.find(" ")
                    num = int(kid[:offset])
                    color = kid[offset : kid.find("bag")].strip()
                    temp[color] = num
                self.items[parent] = temp

    def part1(self, color):
        visited = set()
        stack = set([color])
        while stack:
            temp = [
                k
                for color in stack
                for k, colors in self.items.items()
                if color in colors and k not in visited
            ]
            stack = set(temp)
            visited |= stack
        return len(visited)

    def helper(self, color):
        if not self.items[color]:
            return 1
        return 1 + sum(self.helper(c) * v for c, v in self.items[color].items())

    def part2(self, color):
        return self.helper(color) - 1


def test():
    content = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    target = "shiny gold"
    day7 = Day7(content)
    assert day7.part1(target) == 4
    assert day7.part2(target) == 32


def solve():
    content = open("input/7.txt").read()
    target = "shiny gold"
    day7 = Day7(content)
    print(day7.part1(target))
    print(day7.part2(target))


test()
solve()
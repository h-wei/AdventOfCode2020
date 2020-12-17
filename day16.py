class Day16:
    def __init__(self, content):
        self.rules = []
        self.your = []
        self.near = []
        count = 0
        for line in content.split("\n"):
            if len(line) == 0:
                count += 1
            elif count == 0:
                key, value = line.split(": ")
                items = value.split(" or ")
                rule = []
                for item in items:
                    rule += item.split("-")
                self.rules.append((key, [int(r) for r in rule]))
            elif count == 1:
                items = line.split(",")
                if len(items) > 1:
                    self.your = [int(i) for i in items]
            elif count == 2:
                items = line.split(",")
                if len(items) > 1:
                    self.near.append([int(i) for i in items])

    def part1(self):
        total = 0
        for ticket in self.near:
            for i, v in enumerate(ticket):
                if not any(
                    x0 <= v <= x1 or y0 <= v <= y1 for _, (x0, x1, y0, y1) in self.rules
                ):
                    total += v
        return total

    def part2(self, name):
        invalid = self._check()
        neighbors = [None] * len(self.your)
        for i, ticket in enumerate(self.near):
            if i not in invalid:
                row = self._row(ticket)
                for i, s in enumerate(row):
                    neighbors[i] = s if neighbors[i] is None else (neighbors[i] & s)
        mapper = Day16.sort(neighbors)
        product = 1
        for i, (key, _) in enumerate(self.rules):
            if key.startswith(name):
                product *= int(self.your[mapper[i]])
        return product

    def _check(self):
        invalid = set()
        for i, ticket in enumerate(self.near):
            for v in ticket:
                if not any(
                    x0 <= v <= x1 or y0 <= v <= y1 for _, (x0, x1, y0, y1) in self.rules
                ):
                    invalid.add(i)
                    break
        return invalid

    def _row(self, ticket):
        row = []
        for i, v in enumerate(ticket):
            row.append(
                set(
                    j
                    for j, (_, (x0, x1, y0, y1)) in enumerate(self.rules)
                    if x0 <= v <= x1 or y0 <= v <= y1
                )
            )
        return row

    @staticmethod
    def sort(neighbors):
        stack = [i for i, v in enumerate(neighbors) if len(v) == 1]
        while stack:
            v = stack.pop()
            val = list(neighbors[v])[0]
            for i in range(len(neighbors)):
                if i != v and val in neighbors[i]:
                    neighbors[i].remove(val)
                    if len(neighbors[i]) == 1:
                        stack.append(i)

        return {n: i for i, (n,) in enumerate(neighbors)}


def test():
    content = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
    day16 = Day16(content)
    assert day16.part1() == 71
    # assert day16.part2() ==


def solve():
    content = open("input/16.txt").read()
    day16 = Day16(content)
    print(day16.part1())
    print(day16.part2("departure"))


test()
solve()

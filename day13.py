import math


class Day13:
    def __init__(self, content):
        ts, bus = content.split("\n")
        self.ts = int(ts)
        self.bus = [
            (int(b), (int(b) - i) % int(b))
            for i, b in enumerate(bus.split(","))
            if b != "x"
        ]

    def part1(self):
        best = float("inf")
        ans = 0
        for b, _ in self.bus:
            val = self.ts % b
            if not val:
                return 0
            val = b - val
            if best > val:
                best = val
                ans = val * b
        return ans

    def part2(self):
        # Chinese Remainder Theorem
        # ax + by = gcd(a, b)
        # (mb + r) x + by = gcd(a, b)
        def extended_gcd(a, b):
            if b == 0:
                return a, 1, 0
            q, r = divmod(a, b)
            g, x, y = extended_gcd(b, r)
            return g, y, x - y * q

        B, R = self.bus[0]
        for i in range(1, len(self.bus)):
            b, r = self.bus[i]
            g, x, y = extended_gcd(B, b)
            if (r - b) % g:
                raise ValueError("No solutions")
            x = x * (R - r) // g % b
            R -= x * B
            B = B // g * b
            R %= B
        return (R % B + B) % B


def test():
    content = """939
7,13,x,x,59,x,31,19"""
    day13 = Day13(content)
    assert day13.part1() == 295
    assert day13.part2() == 1068781


def solve():
    content = open("input/13.txt").read()
    day13 = Day13(content)
    print(day13.part1())
    print(day13.part2())


test()
solve()

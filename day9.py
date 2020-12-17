class Day9:
    def __init__(self, content, offset):
        self.nums = [int(i) for i in content.split("\n")]
        self.offset = offset

    def helper(self, i):
        s = set()
        for j in range(i - self.offset, i):
            if self.nums[j] in s:
                return True
            s.add(self.nums[i] - self.nums[j])
        return False

    def part1(self):
        for i in range(self.offset, len(self.nums)):
            if not self.helper(i):
                return self.nums[i]
        return None

    def part2(self, target):
        b, e = 0, 0
        s = self.nums[0]
        while b < len(self.nums):
            if s == target:
                a = self.nums[b : e + 1]
                return min(a) + max(a)
            if s > target:
                s -= self.nums[b]
                b += 1
            else:
                e += 1
                s += self.nums[e]


def test():
    content = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    day9 = Day9(content, 5)
    assert day9.part1() == 127
    assert day9.part2(127) == 62


def solve():
    content = open("input/9.txt").read()
    day9 = Day9(content, 25)
    ans = day9.part1()
    print(ans)
    print(day9.part2(ans))


test()
solve()
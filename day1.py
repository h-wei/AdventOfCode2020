class Day1:
    def __init__(self, content):
        self.numbers = [int(line) for line in content.split("\n")]

    def helper(self, nums, target):
        s = set()
        for x in nums:
            if x in s:
                return (x, target - x)
            s.add(target - x)
        return None

    def part1(self, target):
        ans = self.helper(self.numbers, target)
        return ans[0] * ans[1]

    def part2(self, target):
        for i, x in enumerate(self.numbers):
            temp = self.helper(self.numbers[i + 1 :], target - x)
            if temp:
                return x * temp[0] * temp[1]


def test():
    content = """1721
979
366
299
675
1456"""
    target = 2020
    day1 = Day1(content)
    assert day1.part1(target) == 514579
    assert day1.part2(target) == 241861950


def solve():
    content = open("input/1.txt").read()
    target = 2020
    day1 = Day1(content)
    print(day1.part1(target))
    print(day1.part2(target))


test()
solve()
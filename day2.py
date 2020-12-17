class Day2:
    def __init__(self, content):
        self.passwords = list(self._parse(content))

    def _parse(self, content):
        # 9-11 l: vmbsllkcshmrhklrl
        for line in content.split("\n"):
            for i, c in enumerate(line):
                if c == "-":
                    first = int(line[:i])
                    start = i + 1
                elif c == " ":
                    second = int(line[start:i])
                    start = i + 1
                    letter = line[start]
                    password = line[start + 3 :].strip()
                    break
            yield (first, second, letter, password)

    def part1(self):
        return sum(
            lower <= password.count(letter) <= upper
            for lower, upper, letter, password in self.passwords
        )

    def part2(self):
        return sum(
            (password[first - 1] == letter) ^ (password[second - 1] == letter)
            for first, second, letter, password in self.passwords
        )


def test():
    content = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
    day2 = Day2(content)
    assert day2.part1() == 2
    assert day2.part2() == 1


def solve():
    content = open("input/2.txt").read()
    day2 = Day2(content)
    print(day2.part1())
    print(day2.part2())


test()
solve()
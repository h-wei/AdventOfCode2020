class Day8:
    def __init__(self, content):
        self.prompts = list(self._parse(content))

    def _parse(self, content):
        for item in content.split("\n"):
            c, v = item.split()
            yield c, int(v)

    def part1(self):
        ans = 0
        i = 0
        seen = set()
        while i < len(self.prompts):
            if i in seen:
                return ans, False
            seen.add(i)
            c, v = self.prompts[i]
            if c == "acc":
                ans += v
            elif c == "jmp":
                i = i + v - 1
            i += 1
        return (ans, True)

    def part2(self):
        replace = {"jmp": "nop", "nop": "jmp"}
        for p, value in replace.items():
            jmp = [i for i, v in enumerate(self.prompts) if v[0] == p]
            for j in jmp:
                c, v = self.prompts[j]
                self.prompts[j] = value, v
                ans, found = self.part1()
                if found:
                    return ans
                self.prompts[j] = c, v


def test():
    content = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    day8 = Day8(content)
    assert day8.part1() == (5, False)
    assert day8.part2() == 8


def solve():
    content = open("input/8.txt").read()
    day8 = Day8(content)
    print(day8.part1())
    print(day8.part2())


test()
solve()
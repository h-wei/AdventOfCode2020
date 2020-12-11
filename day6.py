class Day6:
    def __init__(self, content):
        self.content = content
    
    def part1(self):
        count = 0
        s = [0] * 26
        for line in self.content.split('\n'):
            if line == '':
                count += sum(i > 0 for i in s)
                s = [0] * 26
            else:
                for c in line:
                    s[ord(c)-ord('a')] += 1
        else:
            count += sum(i > 0 for i in s)
        return count
            
    def part2(self):
        count = 0
        s = [0] * 26
        person = 0
        for line in self.content.split('\n'):
            if line == '':
                count += sum(i == person for i in s)
                s = [0] * 26
                person = 0
            else:
                person += 1
                for c in line:
                    s[ord(c)-ord('a')] += 1
        else:
            count += sum(i == person for i in s)
        return count
    
def test():
    s = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    day6 = Day6(s)
    assert day6.part1() == 11
    assert day6.part2() == 6


def solve():
    content = open('input/6.txt').read()
    day6 = Day6(content)
    print(day6.part1())
    print(day6.part2())
    
test()
solve()
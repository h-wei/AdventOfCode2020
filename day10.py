from collections import Counter

class Day10:
    def __init__(self, content):
        self.items = sorted([int(line) for line in content.split('\n')])
        self.items = [0] + self.items + [self.items[-1] + 3]
        
    def part1(self):
        c = Counter()
        curr = 0
        for i in range(1, len(self.items)):
            c[self.items[i] - self.items[i-1]] += 1
        return c
    
    def part2(self):
        d = {x: i for i, x in enumerate(self.items)}
        dp = [0] * len(self.items)
        dp[0] = 1
        for i, c in enumerate(self.items):
            for j in range(1, 4):
                if c-j >= 0 and c - j in d:
                    dp[i] += dp[d[c-j]]
        return dp[-1]
            
    
def test():
    content = """16
10
15
5
1
11
7
19
6
12
4"""
    day10 = Day10(content)
    c = day10.part1()
    assert c[1] * c[3] == 35
    assert day10.part2() == 8
    
def solve():
    content = open('input/10.txt').read()
    day10 = Day10(content)
    c = day10.part1()
    print(c[1] * c[3])
    print(day10.part2())
    
test()
solve()
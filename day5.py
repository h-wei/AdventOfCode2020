class Day5:
    def __init__(self, content):
        self.seats = content.split('\n')
        self.ids = sorted([self.take(s) for s in self.seats])
        
    @staticmethod
    def take(s):
        rstart, rend = 0, 128
        cstart, cend = 0, 8
        for c in s:
            if c == 'F':
                rend = (rend + rstart) // 2
            elif c == 'B':
                rstart = (rend + rstart) // 2
            elif c == 'L':
                cend = (cstart + cend) // 2
            else:
                cstart = (cstart + cend) // 2
        return rstart * 8 + cstart
    
    def part1(self):
        return self.ids[-1]
    
    def part2(self):
        start, end = 0, len(self.ids)-1
        while start <= end:
            mid = (start + end) // 2
            if self.ids[mid] - self.ids[start] == mid - start:
                start = mid + 1
            else:
                end = mid -1
        return start + 1
    
def test():
    for s, n in (('FBFBBFFRLR', 357), ('BFFFBBFRRR', 567), ('FFFBBBFRRR', 119), ('BBFFBBFRLL', 820)):
        assert Day5.take(s) == n
    
def solve():
    content = open('input/5.txt').read()
    day5 = Day5(content)
    print(day5.part1())
    print(day5.part2())

test()
solve()
class Day11:
    def __init__(self, content):
        self.grid = [list(x) for x in content.split('\n')]
        
    @staticmethod
    def rule1(g, i, j):
        if g[i][j] == '.':
            return '.'
        
        l = s = 0
        for y in (i-1, i, i+1):
            for x in (j-1, j, j+1):
                if 0 <= y < len(g) and 0 <= x < len(g[0]):
                    if g[y][x] == 'L':
                        l += 1
                    elif g[y][x] == '#':
                        s += 1
                        
        if g[i][j] == 'L' and s == 0:
            return '#'
        if g[i][j] == '#' and s > 4:
            return 'L'
        return g[i][j]
    
    @staticmethod
    def rule2(g, i, j):
        if g[i][j] == '.':
            return '.'
        l = s = 0
        directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0), (1,1))
        for dx, dy in directions:
            x, y = i, j
            while True:
                x, y = x + dx, y + dy
                if 0 <= x < len(g) and 0 <= y < len(g[0]):
                    if g[x][y] == 'L':
                        l += 1
                        break
                    elif g[x][y] == '#':
                        s += 1
                        break
                else:
                    break
    
        if g[i][j] == 'L' and s == 0:
            return '#'
        if g[i][j] == '#' and s >= 5:
            return 'L'
        return g[i][j]
              
    def seat(self, h):
        m, n = len(self.grid), len(self.grid[0])
        a = [r[:] for r in self.grid]
        
        while True:
            aux = [[0 for _ in range(n)] for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    aux[i][j] = h(a, i, j)
            if aux == a:
                return sum(aux[i][j] == '#' for i in range(m) for j in range(n))
            a = aux
            
    def part1(self):
        return self.seat(Day11.rule1)
                
    def part2(self):
        return self.seat(Day11.rule2)
    
def test():
    content = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''
    day11 = Day11(content)
    assert day11.part1() == 37
    assert day11.part2() == 26
    
def solve():
    content = open('input/11.txt').read()
    day11 = Day11(content)
    print(day11.part1())
    print(day11.part2())
    
test()
solve()
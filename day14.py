class Day14:
    def __init__(self, content):
        self.actions = []
        for line in content.split('\n'):
            if line[:2] == 'ma':
                _, mask = line.split(' = ')
                self.actions.append((mask,))
            else:
                s, value = line.split(' = ')
                index = s[4:-1]
                self.actions.append((int(index), int(value)))

    def part1(self):
        d = {}
        op_or, op_and = 0, 0
        for action in self.actions:
            if len(action) > 1:
                i, v = action
                d[i] = v & op_and | op_or
            else:
                op_or, op_and = int(action[0].replace('X', '0'), 2), int(action[0].replace('X', '1'), 2)
        return sum(d.values())

    def part2(self):
        d = {}
        mask = 0
        position = []
        for action in self.actions:
            if len(action) > 1:
                i, v = action
                value = (i | int(mask.replace('X', '0'), 2)) & (int(mask.replace('0', '1').replace('X', '0'), 2))
                for j in range(1<<len(position)):
                    k = Day14.helper(value, j, position)
                    d[k] = v
            else:
                mask = action[0]
                position = [i for i, c in enumerate(mask[::-1]) if c == 'X']
        return sum(d.values())
    
    @staticmethod
    def helper(value, offset, position):
        i = 0
        while offset > 0:
            if offset & 1:
                value += 1 << position[i]
            offset >>= 1
            i += 1
        return value

def test():
    content = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    day14 = Day14(content)
    assert day14.part1() == 165
    content = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    day14 = Day14(content)
    assert day14.part2() == 208

def solve():
    content = open('input/14.txt').read()
    day14 = Day14(content)
    print(day14.part1())
    print(day14.part2())

test()
solve()

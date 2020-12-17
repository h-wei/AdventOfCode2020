class Day4:
    def __init__(self, content):
        self.passports = list(self._parse(content))

    def _parse(self, content):
        item = []
        for line in content.split("\n"):
            if line == "":
                yield dict(items.split(":") for items in " ".join(item).split())
                item = []
            else:
                item.append(line)
        else:
            yield dict(items.split(":") for items in " ".join(item).split())

    def part1(self):
        keywords = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
        return sum(keywords <= set(passport.keys()) for passport in self.passports)

    def part2(self):
        def valid(passport):
            """
            byr (Birth Year) - four digits; at least 1920 and at most 2002.
            iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
            hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            pid (Passport ID) - a nine-digit number, including leading zeroes.
            cid (Country ID) - ignored, missing or not.
            """
            if not ("byr" in passport and 1920 <= int(passport["byr"]) <= 2002):
                return False
            if not ("iyr" in passport and 2010 <= int(passport["iyr"]) <= 2020):
                return False
            if not ("eyr" in passport and 2020 <= int(passport["eyr"]) <= 2030):
                return False
            if "hgt" not in passport:
                return False
            height, unit = int(passport["hgt"][:-2]), passport["hgt"][-2:]
            if not (
                (unit == "cm" and 150 <= height <= 193)
                or (unit == "in" and 59 <= height <= 76)
            ):
                return False
            if not (
                "hcl" in passport
                and passport["hcl"][0] == "#"
                and len(passport["hcl"]) == 7
                and all(i in "0123456789abcdef" for i in passport["hcl"][1:])
            ):
                return False
            if not (
                "ecl" in passport
                and passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            ):
                return False
            if not (
                "pid" in passport
                and len(passport["pid"]) == 9
                and all("0" <= i <= "9" for i in passport["pid"])
            ):
                return False
            return True

        return sum(valid(passport) for passport in self.passports)


def test():
    content = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
    day4 = Day4(content)
    assert day4.part1() == 2


def solve():
    content = open("input/4.txt").read()
    day4 = Day4(content)
    print(day4.part1())
    print(day4.part2())


test()
solve()
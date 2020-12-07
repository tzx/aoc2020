import fileinput
from collections import defaultdict
import re

inp = [line.strip() for line in fileinput.input()]


res = 0
d = defaultdict(int)

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

for i in inp:
    if i == '':
        if len(d) == 7:
            res += 1
        d = defaultdict(int)
    else:
        kvs = i.split()
        for kv in kvs:
            k, v = kv.split(":")
            if k in fields:
                valid = True
                if k == "byr":
                    if not (1920 <= int(v) <= 2002):
                        valid = False
                elif k == "iyr":
                    if not (2010 <= int(v) <= 2020):
                        valid = False
                elif k == "eyr":
                    if not (2020 <= int(v) <= 2030):
                        valid = False
                elif k == "hgt":
                    if v.endswith("cm"):
                        if not (150 <= int(v[:-2]) <= 193):
                            valid = False
                    elif v.endswith("in"):
                        if not (59 <= int(v[:-2]) <= 76):
                            valid = False
                    else:
                        valid = False

                elif k == "hcl":
                    if len(v) != 7 or v[0] != '#' or any([c not in "0123456789abcdef" for c in v[1:]]):
                        valid = False
                elif k == "ecl":
                    if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        valid = False
                elif k == "pid":
                    if len(v) != 9 or any([c not in "0123456789" for c in v]):
                        valid = False
                    
                if valid:
                    d[k] += 1
    
print(res)

import fileinput
import re

p1 = 0
p2 = 0
passport = {} # current passport

def in_range(s, lo, hi):
    return lo<=int(s)<=hi

lines = list(fileinput.input())
lines.append('')
for line in lines:
    line = line.strip()
    if not line:
        valid1 = all([f in passport for f in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])
        if valid1:
            p1 += 1
            valid2 = True

            if not in_range(passport['byr'], 1920, 2002):
                valid2 = False
            if not in_range(passport['iyr'], 2010, 2020):
                valid2 = False
            if not in_range(passport['eyr'], 2020, 2030):
                valid2 = False

            ht = passport['hgt']
            if ht.endswith('in'):
                if not in_range(ht[:-2], 59, 76):
                    valid2 = False
            elif ht.endswith('cm'):
                if not in_range(ht[:-2], 150, 193):
                    valid2 = False
            else:
                valid2 = False

            hcl = passport['hcl']
            if hcl[0]!='#' or any([c not in '0123456789abcdef' for c in hcl[1:]]):
                valid2 = False

            ecl = passport['ecl']
            if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid2 = False

            pid = passport['pid']
            if len(pid) != 9 or any([c not in '0123456789' for c in pid]):
                valid2 = False

            if valid2:
                p2 += 1
        passport = {}
    else:
        words = line.split()
        for word in words:
            k,v = word.split(':')
            passport[k] = v

print('\n\n')
print(p2)


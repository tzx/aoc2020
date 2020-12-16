import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin.read().split('\n\n')]

rules = dict()
for rule in lines[0].split('\n'):
    chunks = re.match(r'(\w+ ?\w*): (\d+-\d+) or (\d+-\d+)', rule)
    name = chunks[1]
    range1a, range1b = chunks[2].split('-')
    range2a, range2b = chunks[3].split('-')

    rules[name] = ((int(range1a), int(range1b)), (int(range2a), int(range2b)))

def inrange(i, a, b):
    return a <= i <= b


res = 0
valid = collections.defaultdict(set)
for nb in lines[2].split('\n')[1:]:
    nums = nb.split(',')
    for i,num in enumerate(nums):
        num = int(num)
        in_range = False
        for ranges in rules.values():
            range1, range2 = ranges
            if inrange(num, range1[0], range1[1]) or inrange(num, range2[0], range2[1]):
                in_range = True
                break
        # if not in_range:
        #     res += num
        if in_range:
            valid[i].add(num)

fieldtoidx = collections.defaultdict(set)
unsatisfied = list(valid.keys())
while len(unsatisfied) != 0:
    pos = unsatisfied[-1]
    
    for rule, ranges in rules.items():
        range1, range2 = ranges
        good = True
        for seat in valid[pos]:
            if not (inrange(seat, range1[0], range1[1]) or inrange(seat, range2[0], range2[1])):
                good = False
                break
        if good:
            fieldtoidx[rule].add(pos)
    unsatisfied.pop()

count = 0
while count != len(fieldtoidx):
    count = 0
    for rule, valididx in fieldtoidx.items():
        if len(valididx) == 1:
            count += 1
            item = list(valididx)[0]
            for r, idx in fieldtoidx.items():
                if r != rule and item in idx:
                    idx.remove(item)

res = 1
for field, idx in fieldtoidx.items():
    if field.startswith('departure'):
        idx = list(idx)[0]
        res *= int(lines[1].split('\n')[1].split(',')[idx])
print(res)


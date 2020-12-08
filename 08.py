import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin]
cp = lines[:]

to_change = [x for x, i in enumerate(lines) if i.split()[0] == "nop" or i.split()[0] == "jmp"]


for change in to_change:
    op = lines[change].split()[0]
    if op == "nop":
        lines[change] = lines[change].replace("nop", "jmp")
    else:
        lines[change] = lines[change].replace('jmp', 'nop')
    # print(lines)

    res = 0
    i = 0
    visited = set()
    bad = False
    while i < len(lines):
        if i in visited:
            bad = True
            break
        else:
            visited.add(i)
        op, val = lines[i].split()
        if op == "nop":
            i += 1
        elif op == "acc":
            res += int(val)
            i += 1
        else:
            i += int(val)
    if not bad:
        print(res)
    else:
        lines = cp[:]

#print(res)

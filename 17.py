import copy
import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin]

z = dict()

active = set()
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == '#':
            active.add((i, j, 0, 0))



def get_range(idx, S):
    # Need +2 because range is not end inclusive, so we +1 to +1
    return range(min(p[idx] for p in S) - 1, max(p[idx] for p in S) + 2)

cycle = 0
while cycle < 6:
    new_active = set()

    for x in get_range(0, active):
        for y in get_range(1, active):
            for z in get_range(2, active):
                for w in get_range(3, active):
                    count = 0
                    for di in (-1, 0, 1):
                        for dj in (-1, 0, 1):
                            for dk in (-1, 0, 1):
                                for dw in (-1, 0, 1):
                                    if di == dj == dk == dw == 0:
                                        continue
                                    if (x+di, y+dj, z+dk, w+dw) in active:
                                        count += 1
                    if (x, y, z, w) in active:
                        if count == 2 or count == 3:
                            new_active.add((x, y, z, w))
                            print('stay', (x, y, z, w))
                    else:
                        if count == 3:
                            new_active.add((x, y, z, w))
    active = new_active
    print(active)
    cycle += 1

print(len(active))

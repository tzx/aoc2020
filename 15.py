import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin]
lines = lines[0].split(',')

lu = dict()

for i, l in enumerate(lines):
    lu[int(l)] = (-int(1), i+1)

print(lu)

most_recent = int(lines[-1])

i = len(lines) + 1

while i <= 30000000:
    last_spoked = lu[most_recent]
    if last_spoked[0] == -1:
        most_recent = 0
    else:
        most_recent = last_spoked[1] - last_spoked[0]
    if most_recent in lu:
        lu[most_recent] = (lu[most_recent][1], i)
    else:
        lu[most_recent] = (-1, i)
    i += 1

print(most_recent)



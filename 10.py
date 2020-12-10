import sys
import math
import collections
import re

lines = [int(l.rstrip("\n")) for l in sys.stdin]

res = 0

builtin = max(lines) + 3

lines.sort()

dif1 = 0
dif2 = 0
dif3 = 0

prev = 0
for l in lines:
    if l - prev == 3:
        dif3 += 1
    elif l - prev == 2:
        dif2 += 1
    elif l - prev == 1:
        dif1 += 1
    else:
        print("ERR")
    prev = l
    
print((dif3+1) * dif1)


to_idx = dict()
for i, l in enumerate(lines):
    to_idx[l] = i+1
to_idx[0] = 0

num_of_ways = [0] * (len(lines) + 2)
num_of_ways[0] = 1

lines.insert(0, 0)

lines.append(builtin)

for i, l in enumerate(lines):
    if i == 0:
        continue
    if l - 3 in to_idx:
        num_of_ways[i] += num_of_ways[to_idx[l-3]]
    if l - 2 in to_idx:
        num_of_ways[i] += num_of_ways[to_idx[l-2]]
    if l - 1 in to_idx:
        num_of_ways[i] += num_of_ways[to_idx[l-1]]



print(num_of_ways)

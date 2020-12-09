import sys
import math
import collections
import re

lines = [int(l.rstrip("\n")) for l in sys.stdin]

preamble = []
size = 25
for i,l in enumerate(lines):
    if i < size:
        preamble.append(int(l))
    else:
        valid = False
        for a in range(len(preamble)):
            if valid:
                break
            for b in range(len(preamble)):
                if a != b:
                    if preamble[a] + preamble[b] == l:
                        valid = True
                        preamble.pop(0)
                        preamble.append(int(l))
                        break
        if not valid:
            print(l)
            break
                        

i = 0
j = 0
while i < len(lines):
    sum_ = 0
    while sum_ < 542529149:
        sum_ += lines[j]
        j += 1
    if sum_ == 542529149:
        min_ = min(lines[i:j])
        max_ = max(lines[i:j])
        print(min_ + max_)
        break
    i += 1
    j = i





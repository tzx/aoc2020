import sys
import re

lines = [l.rstrip("\n") for l in sys.stdin]


res = 0

aall = set(i * 8 + j for i in range(1, 126) for j in range(7))
print(aall)

ids = set()
for l in lines:
    lo = 0
    hi = 127
    
    colo = 0
    cohi = 7
    for letter in l:
        if letter == 'F':
            hi = (hi + lo) // 2
        elif letter == 'B':
            lo = (hi +lo) //2 + 1
        elif letter == 'L':
            cohi = (cohi + colo) //2
        elif letter == 'R':
            colo = (cohi + colo) //2 +1

    ids.add(hi * 8 + cohi)
    res = max(res, hi * 8 + cohi)



print(aall-ids)
print(res)

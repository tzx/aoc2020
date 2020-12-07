import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin.read().split('\n\n')]

print(lines)


res = 0

for group in lines:
    count = group.count('\n') + 1
    qanswered = collections.defaultdict(int)
    for letter in group:
        if letter != '\n':
            qanswered[letter] += 1

    valid = True
    for letter in qanswered:
        if qanswered[letter] == count:
            res += 1

print(res)

    

import copy
import sys
import math
import collections
import re


p1, p2 = [l.rstrip('\n') for l in sys.stdin.read().split('\n\n')]

p1deck = p1.split('\n')[1:]
p1deck = [int(x) for x in p1deck]
p2deck = p2.split('\n')[1:]
p2deck = [int(x) for x in p2deck]

ogsize = len(p1deck)


def recurse(p1deck, p2deck):
    seen = set()
    while len(p1deck) != 0 and len(p2deck) != 0:
        cfg = (tuple(p1deck), tuple(p2deck))
        if cfg in seen:
            return "p1"
        seen.add(cfg)

        p1t = p1deck.pop(0)
        p2t = p2deck.pop(0)

        if len(p1deck) >= p1t and len(p2deck) >= p2t:
            res = recurse(p1deck[:p1t], p2deck[:p2t])
            winner = res
        else:
            winner = "p1" if p1t>p2t else "p2"

        if winner == "p1":
            p1deck.append(p1t)
            p1deck.append(p2t)
        else:
            p2deck.append(p2t)
            p2deck.append(p1t)
    return "p1" if p1deck else "p2"


recurse(p1deck, p2deck)

if p1deck:
    fulldeck = p1deck
else:
    fulldeck = p2deck
res = 0

for i in reversed(range(len(fulldeck))):
    res += (i+1) * int(fulldeck[len(fulldeck)-1 - i])

print(res)

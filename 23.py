import copy
import sys
import math
import collections
import re

# inp = list("523764819")
inp = list('523764819')
inp = list(map(int, inp))

current = inp[0]
cidx = 0
for _ in range(100):

    pup = []
    # for i in range(cidx + 1, cidx + 4):
    #     i = i % len(inp)
    #     pup.append(inp[i])
    # pup = inp[cidx + 1:cidx + 4]
    # del inp[cidx + 1:cidx + 4]
    idd = (cidx + 1) % len(inp)
    for i in range(3):
        pup.append(inp[idd])
        idd = (idd + 1) % len(inp)
    assert len(pup) == 3
    for p in pup:
        inp.remove(p)


    dest = current - 1
    while dest in pup or dest < min(inp):
        dest -= 1
        if dest < min(inp):
            dest = max(inp)
    idx_dest = inp.index(dest)

    inp = inp[:idx_dest+1] + pup + inp[idx_dest+1:]
    current = inp[(inp.index(current)+1) % len(inp)]
    cidx = inp.index(current)

idx1 = inp.index(1)
i = (idx1 + 1) % len(inp)
res = []
while i != idx1:
    res.append(str(inp[i]))
    i = (i + 1) % len(inp)

print("".join(res))


inp = list('523764819')
inp = list(map(int, inp))
cups = int(1e6)
order = [i for i in inp] + list(range(10, cups + 1))
# order.extend(range(10, cups+1))

class LL:
    def __init__(self, v):
        self.v = v
        self.next = None

i2ll = dict()

# 1 idx
for i in range(1, cups + 1):
    i2ll[i] = LL(i)
for i in range(len(order)):
    i2ll[order[i]].next = i2ll[order[(i+1)%len(order)]] #wraps last one

current = i2ll[order[0]]
for _ in range(int(1e7)):
    nxt_start = current.next
    current.next = current.next.next.next.next

    dest = current.v - 1
    while dest in (nxt_start.v, nxt_start.next.v, nxt_start.next.next.v) or dest <= 0:
        dest -= 1
        if dest <=0:
            dest = cups

    lldest = i2ll[dest]
    nxt_start.next.next.next = lldest.next
    lldest.next = nxt_start

    current = current.next

print(i2ll[1].next.v * i2ll[1].next.next.v)

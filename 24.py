import copy
import sys
import math
import collections
import re


lines = [l.rstrip('\n') for l in sys.stdin]

# nw, ne, e
black_tiles = set()

for l in lines:
    current = ''
    nw, ne = 0, 0
    for c in l:
        current += c
        if c in 'ns':
            continue
        
        if current == 'e':
            ne += 1
            nw -= 1
        elif current == 'w':
            ne -= 1
            nw += 1
        elif current == 'ne':
            ne += 1
        elif current == 'nw':
            nw += 1
        elif current == 'se':
            nw -= 1
        elif current == 'sw':
            ne -= 1
        else:
            print(current)
            assert False
        current = ''


    if (nw, ne) in black_tiles:
        black_tiles.remove((nw, ne))
    else:
        black_tiles.add((nw, ne))

print(len(black_tiles))

dirs = [(1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(100):
    changed = black_tiles.copy()

    neighbors = set()
    for nw, ne in black_tiles:
        neighbors.add((nw, ne))
        for dnw, dne in dirs:
            neighbors.add((nw + dnw, ne + dne))

    for nw, ne in neighbors:
        cnt = 0
        for dnw, dne in dirs:
            if (nw+dnw, ne+dne) in black_tiles:
                cnt += 1
        if (nw,ne) in black_tiles:
            if cnt > 2 or cnt == 0:
                changed.remove((nw, ne))
        else:
            if cnt == 2:
                changed.add((nw, ne))
    black_tiles = changed

print(len(black_tiles))

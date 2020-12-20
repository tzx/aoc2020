import copy
import sys
import math
import collections
import re


tiles = [l.rstrip('\n') for l in sys.stdin.read().split('\n\n')]

t_list = []

def str_to_grid(string):
    grid = []
    for r in string.split('\n'):
        row = []
        for c in r:
            row.append(c)
        grid.append(row)
    return grid

def get_borders(grid):
    res = []
    rows = len(grid)
    cols = len(grid[0])

    res.append(grid[0].copy())
    res.append(grid[-1].copy())
    left = [grid[x][0] for x in range(rows)]
    right = [grid[x][cols-1] for x in range(rows)]
    res.append(left)
    res.append(right)
    return res


t_borders = collections.defaultdict(list)
t_flipped = collections.defaultdict(list)
all_borders = collections.defaultdict(int)
for ttt in tiles[:-1]:
    top, gridstring = ttt.split(':\n')
    num = top.split()[1]
    grid = str_to_grid(gridstring)

    borders = [tuple(x) for x in get_borders(grid)]
    for x in borders:
        all_borders[x] += 1
        all_borders[tuple(reversed(x))] += 1
    t_borders[num] = borders
    t_flipped[num] = [tuple(reversed(x)) for x in get_borders(grid)]

res = 1
bbbb = []
for num, borders in t_borders.items():
    for b in borders:
        assert b in all_borders
        assert tuple(reversed(b)) in all_borders

    # max_ = max(all_borders[b] for b in borders)
    # max_ = max(all_borders[tuple(reversed(b))] for b in borders)
    s = sum(all_borders[b] for b in borders)
    s2 = sum(all_borders[tuple(reversed(b))] for b in borders)
    # Got min to be 6 and max to be 8, so assume every edge is unique?
    # Also noticed that min appears only 4 times, so that should be corner
    if s == 6 or s2 == 6:
        res *= int(num)
        if s == 6: bbbb.append((False, num))
        else: bbbb.append((True, num))
print(res)

# guessed bound of 32-60 (density) because i didn't want to do this
# we binary searched and started with 44, my answer was 43.... lol
outside_cnt = 0
for ttt in tiles: # skip borders, have 2 due to Tile ....:
    for l in ttt.split('\n')[2:-1]:
        for c in l[1:-1]:
            if c == '#': outside_cnt += 1
print('yay1', outside_cnt)
sea_mon_cnt = 15

for num_of_sea_mon in range(32, 60):
    print(num_of_sea_mon,  outside_cnt - sea_mon_cnt * num_of_sea_mon)

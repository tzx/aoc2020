import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin]

table = []

for l in lines:
    li = []
    for cr in l:
        li.append(cr)
    table.append(li)
print(table[0])


def copy2d(tb):
    ret = []
    for l in tb:
        row = []
        for c in l:
            row.append(c)
        ret.append(row)
    return ret

def sees(i, j):
    count = 0
    for col in range(j + 1, len(table[i])):
        if table[i][col] == 'L':
            break
        elif table[i][col] == '#':
            count += 1
            break
    for col in range(j - 1, -1, -1):
        if table[i][col] == 'L':
            break
        elif table[i][col] == '#':
            count += 1
            break
    for row in range(i + 1, len(table)):
        if table[row][j] == 'L': break
        elif table[row][j] == '#':
            count += 1
            break
    for row in range(i - 1, -1, -1):
        if table[row][j] == 'L': break
        elif table[row][j] == '#':
            count += 1
            break

    row, col = i - 1, j - 1
    while row >= 0 and col >= 0:
        if table[row][col] == 'L': break
        elif table[row][col] == '#':
            count += 1
            break
        row -= 1
        col -= 1
        
    row, col = i + 1, j - 1
    while row < len(table) and col >= 0:
        if table[row][col] == 'L': break
        elif table[row][col] == '#':
            count += 1
            break
        row += 1
        col -= 1

    row, col = i - 1, j + 1
    while row >= 0 and col < len(table[i]):
        if table[row][col] == 'L': break
        elif table[row][col] == '#':
            count += 1
            break
        row -= 1
        col += 1

    row, col = i + 1, j + 1
    while row < len(table) and col < len(table[i]):
        if table[row][col] == 'L': break
        elif table[row][col] == '#':
            count += 1
            break
        row += 1
        col += 1
    return count

res = 0
# 
change = False
while True:
    t = copy2d(table)
    for i, row in enumerate(table):
        for j, col in enumerate(table[i]):
            if col == 'L':
                # empty_adjacent = True
                # if j > 0 and table[i][j-1] == '#':
                #     empty_adjacent = False
                # if j < len(table[i])-1 and table[i][j+1] == '#':
                #     empty_adjacent = False
                # if i > 0 and table[i-1][j] == '#':
                #     empty_adjacent = False
                # if i < len(table) - 1 and table[i+1][j] == '#':
                #     empty_adjacent = False

                # if j > 0 and i > 0 and table[i-1][j-1] == '#':
                #     empty_adjacent = False
                # if j > 0 and i < len(table) - 1 and table[i+1][j-1] == '#':
                #     empty_adjacent = False
                # if j < len(table[i]) - 1 and i < len(table) - 1 and table[i+1][j+1] == '#':
                #     empty_adjacent = False
                # if j < len(table[i]) -1 and i > 0 and table[i-1][j+1] == '#':
                #     empty_adjacent = False

                # if empty_adjacent:
                #     t[i][j] = '#'
                #     change = True
                count = sees(i, j)
                if i == 0 and j == 3:
                    print(count)
                if count == 0:
                    t[i][j] = '#'
                    change = True
            elif col == '#':
                # count = 0
                # if j > 0 and table[i][j-1] == '#':
                #     count += 1
                # if j < len(table[i])-1 and table[i][j+1] == '#':
                #     count += 1
                # if i > 0 and table[i-1][j] == '#':
                #     count += 1
                # if i < len(table) - 1 and table[i+1][j] == '#':
                #     count += 1

                # if j > 0 and i > 0 and table[i-1][j-1] == '#':
                #     count += 1
                # if j > 0 and i < len(table) - 1 and table[i+1][j-1] == '#':
                #     count += 1
                # if j < len(table[i]) - 1 and i < len(table) - 1 and table[i+1][j+1] == '#':
                #     count += 1
                # if j < len(table[i]) -1 and i > 0 and table[i-1][j+1] == '#':
                #     count += 1
                count = sees(i, j)
                if count >= 5:
                    t[i][j] = 'L'
                    change = True

    print(t[0])
    table = t
    if change:
        change = False
        res += 1
    else:
        break

res = 0
for r in table:
    for c in r:
        if c == '#': res += 1
print(res)


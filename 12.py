import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin]
res = 0
x, y = 0, 0
i, j = 10, 1
direction = 90

for l in lines:
    action, num = l[:1], int(l[1:])

    if action in { 'L', 'R' }:
        direction = num
        if action == 'L':
            direction = -direction;
            direction = direction % 360
        if direction == 90:
            i, j = j, -i
        elif direction == 270:
            i, j = -j, i
        elif direction == 180:
            i, j = -i, -j
        else:
            print("?")

    else:
        movement = None
        if action == 'N':
            movement = (0, num)
        elif action == 'S':
            movement = (0, -num)
        elif action == 'E':
            movement = (num, 0)
        elif action == 'W':
            movement = (-num, 0)

        if movement:
            i += movement[0]
            j += movement[1]
        else:
           # if direction == 0:
           #     y += num
           # elif direction == 90:
           #     x += num
           # elif direction == 180:
           #     y -= num
           # elif direction == 270:
           #     x -= num
           # else:
           #     print('??')
           x += num * i
           y += num * j

print(abs(x) + abs(y))


import copy
import sys
import math
import collections
import re


d = 20201227
key1, key2 = [l.rstrip('\n') for l in sys.stdin]

def transform(snum, key):
    i = 1
    loopsize = 0
    while True:
        i *= snum
        i = i % d
        loopsize += 1
        if i == key:
            return (i, loopsize)

a, k1size = transform(7, int(key1))
b, k2size = transform(7, int(key2))

assert a == int(key1)
assert b == int(key2)

ekey = pow(int(key1), k2size, d)
ekey2 = pow(int(key2), k1size, d)
assert ekey == ekey2

print(ekey)

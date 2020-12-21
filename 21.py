import copy
import sys
import math
import collections
import re


lines = [l.rstrip('\n') for l in sys.stdin]

a2i = collections.defaultdict(set)
nice = set()
for l in lines:
    ingredients, allergens = l.split(' (contains ')
    allergens = allergens[:-1]

    ings = set(ingredients.split())
    nice |= ings

    for a in allergens.split(', '):
        if a not in a2i:
            a2i[a] = ings
        else:
            a2i[a] &= ings

nice = nice - set(ing for ings in a2i.values() for ing in ings)
res = 0
for l in lines:
    ingredients, allergens = l.split(' (contains ')
    allergens = allergens[:-1]
    ings = ingredients.split()
    algs = allergens.split(', ')
    for ing in ings:
        if ing in nice:
            res += 1
print(res)

# a2ii is to one actual ingredient rather than possible, i suck at naming
a2ii = dict()
while len(a2ii) < len(a2i):
    for a, ings in a2i.items():
        if len(ings) == 1:
            a2ii[a] = list(ings)[0]
            for aa, iings in a2i.items():
                if a != aa:
                    iings -= ings

for ings in a2i.values():
    assert len(ings) == 1

print(','.join(value for _,value in sorted(a2ii.items())))

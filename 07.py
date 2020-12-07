import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin]


res = 0

old_available = 0
new_available = 1

can_contain = set()
contains = { 'shiny gold' }
while old_available != new_available:
    for group in lines:
        words = group.split()
        chunk = re.findall(r'((\d+) (\w+ \w+) bag)', group)
        for c in chunk:
            adj = c[1]
            if adj in contains:
                contains.add(words[0] + ' ' + words[1])

    old_available = new_available
    new_available = len(contains)




G = collections.defaultdict(list) 

for group in lines:
    bag = ' '.join(group.split()[:2])
    chunk = re.findall(r'((\d+) (\w+ \w+) bag)', group)
    for c in chunk:
        num = int(c[1])
        adj = c[2]
        G[bag].append((adj, num))

q = collections.deque()
q.append(('shiny gold', 1))


res = 0
while q:
    bag = q.popleft()
    res += bag[1]
    for inside, num in G[bag[0]]:
        q.append((inside, bag[1] * num))


# print(new_available)
print(res)

    

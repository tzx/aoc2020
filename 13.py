import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin]
earliest = int(lines[0])
bus_ids = lines[1].split(',')

print(earliest)
print(bus_ids)
res = 0

min_ = float('inf')
best = None

for idd in bus_ids:
    if idd != 'x':
        idd = int(idd)
        time = math.ceil(earliest / idd) * idd
        if time - earliest < min_:
            min_ = time - earliest
            best = idd

    

print(best * min_)



req = []
for i, num in enumerate(bus_ids):
    if num == 'x': continue

    num = int(num)
    req.append((i, num))

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


res = 0
s = req[0][1]
num_valid = 1

while num_valid < len(req):
    r = req[num_valid]
    offset = r[0]
    num = r[1]
    if (res+offset) % num == 0:
        s = lcm(s, num)
        num_valid += 1
    else:
        res += s

print(res)

def egcd_modinv(a, m):
    r_0, r_1 = a, m
    s_0, s_1 = 1, 0
    while r_1 != 0:
        q = r_0 // r_1
        r_0, r_1 = r_1, r_0 - q * r_1
        s_0, s_1 = s_1, s_0 - q * s_1
    if s_0 < 0:
        s_0 += m
    return s_0

# Let's actually solve by construction rather than by sieving
req = []
N = 1
for i, num in enumerate(bus_ids):
    if num == 'x': continue
    num = int(num)
    N *= num
    req.append((-i, num))

res = 0
for a, n in req:
    N_i = N // n

    # Use Euler's Theorem to find the inverse
    M_i = pow(N_i, n - 2, n)
    # Check with finding inverse using Extended Euclid
    assert M_i == egcd_modinv(N_i, n)

    res += a * M_i * N_i
res %= N
print(res)

import sys

res = 0

# for line in sys.stdin:

entries = []
for line in sys.stdin:
    entries.append(int(line))

for i in entries:
    for j in entries:
        for k in entries:
            if i + j + k == 2020:
                print(i, j, k)
                print(i * j * k)



print(res)

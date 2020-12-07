import sys

res = 0

mins = []
maxs=[]
letter=[]
passwords=[]


for line in sys.stdin:
    a, b, c = line.split(" ")

    min_, max_ = a.split("-")
    mins.append(min_)
    maxs.append(max_)

    letter.append(b[0])

    passwords.append(c.strip())

for i in range(len(mins)):
    min_, max_ = int(mins[i]), int(maxs[i])

    l = letter[i]
    
    p = passwords[i]

    count = 0
    if p[min_-1] == l:
        count += 1
    if p[max_-1] == l:
        count += 1
    

    if count == 1:
        res += 1


print(res)

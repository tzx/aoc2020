import fileinput

all_numbers = r'-?\d+'


c = 0
prev = '.'
trees = 0
row = 0
col = 0

x = [line.strip() for line in fileinput.input()]


lr = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


res = 1
for right, down in lr:
    col = 0
    trees = 0
    for r in x[::down]:
        if r[col % len(r)] == '#':
            trees += 1
        col += right
    print(trees)
    res *= trees




print(res)

import copy
import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin]
res = 0

stack = []
ops = []
for l in lines:
    l = "(" + l.replace(" ", "") + ")"
    # offset = 0
    # for idx in mult_idx:
    #     l = '(' + l[:idx+offset] + ')' + '*' + '(' + l[idx+1+offset:] + ')'
    #     print(l)
    #     offset += 3
    # print(l)


    for c in l:
        if c == '+' or c == '*':
            ops[-1].append(c)
        elif c.isdigit():
            stack[-1].append(c)
        elif c == '(':
            stack.append([])
            ops.append([])
        elif c == ')':
            nums = stack.pop()
            actions = ops.pop()

            # add_idx = [i for i in range(len(actions)) if actions[i] == '+']
            offset = 0
            for idx, action in enumerate(actions):
                if action == '+':
                    new_num = int(nums[idx-offset]) + int(nums[idx-offset+1])
                    nums.pop(idx-offset)
                    nums.pop(idx-offset)
                    nums.insert(idx-offset, new_num)
                    offset += 1
            actions = [i for i in actions if i == '*']


            start = int(nums[0])
            for i, action in enumerate(actions):
                if action == '*':
                    start *= int(nums[i+1])
                else:
                    start += int(nums[i+1])
                
            if stack: stack[-1].append(start)
            else: 
                res += start
        else:
            assert False


print(res)

import copy
import sys
import math
import collections
import re

rulestr, strings = [l.rstrip("\n") for l in sys.stdin.read().split('\n\n')]

rules = {}
for rule in rulestr.split('\n'):
    num, val = rule.split(': ')
    num = int(num)

    if '"' in val:
        assert val[0] == val[2] == '"'
        rules[num] = val[1]
    else:
        ugly_options = val.split(' | ')
        options = []
        for option in ugly_options:
            options.append(option.split())
        rules[num] = options

def matches(string, rulenums):
    if len(string) == 0 or len(rulenums) == 0:
        return len(string) == len(rulenums)
    
    assert isinstance(rulenums[0], int) or rulenums[0].isdigit()
    num = int(rulenums.pop(0))
    if type(rules[num]) is str:
        if string[0] == rules[num]:
            return matches(string[1:], rulenums)
        return False
    else:
        for option in rules[num]:
            if matches(string, option + rulenums):
                return True
    return False

res = 0

# part 2
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]


assert len(rules[0]) == 1
rulenums0 = rules[0][0]
for string in strings.split('\n'):
    if matches(string, rulenums0.copy()):
        res += 1

print(res)

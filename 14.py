import sys
import math
import collections
import re

lines = [l.rstrip("\n") for l in sys.stdin]

addr = dict()

# onemask = 0
# zeromask = 0

for l in lines:
    if l.startswith('mask'):
        mask = l.split()[-1]
        # onemask = ''
        # zeromask = ''

        erase_mask = ''
        masks = ['']

        for v in mask:
            new = []
            if v == 'X':
                for m in masks:
                    new.append(m + '1')
                    new.append(m + '0')
                erase_mask += '1'
            else:
                for m in masks:
                    new.append(m + v)
                erase_mask += '1' if v == '1' else '0'
            masks = new

        # for v in mask:
        #     if v == 'X':
        #         onemask += '0'
        #         zeromask += '1'
        #     else:
        #         if v == '1':
        #             onemask += '1'
        #             zeromask += '1'
        #         else:
        #             zeromask += '0'
        #             onemask += '0'
        erase_mask = int(erase_mask, 2)
        # onemask = int(onemask, 2)
        # zeromask = int(zeromask, 2)
    elif l.startswith('mem'):
        globs = re.match(r'mem\[(\d+)\] = (\d+)', l)
        a, val = int(globs[1]), int(globs[2])

        erased = a & ~erase_mask
        for m in masks:
            m = int(m, 2)
            k = erased | m
            addr[k] = val

        # val |= onemask
        # val &= zeromask
        # print(format(onemask, 'b'))
        # print(format(zeromask, 'b'))
        # print(format(val, 'b'))
    else:
        assert False

res = sum(v for _,v in addr.items() if v != 0)


print(res)

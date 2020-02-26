#!/usr/bin/env python3

import sys
from functools import reduce

def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt,0) + 1
    return acc

print(reduce(make_counts, sys.stdin, {}))

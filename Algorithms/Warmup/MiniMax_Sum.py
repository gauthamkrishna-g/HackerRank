#!/bin/python

import sys

x = list(map(int, input().strip().split(' ')))
maximum = sum(x) - max(x)
minimum = sum(x) - min(x)
print(maximum, minimum)

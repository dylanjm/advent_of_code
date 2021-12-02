#!/usr/bin/env python3

with open('inputs/input0101.txt') as f:
    data = [int(line) for line in f.readlines() if line.strip()]

ans1 = sum(j > i for i,j in zip(data, data[1:]))
xy = [sum(x) for x in zip(data, data[1:], data[2:])]
ans2 = sum(j > i for i,j in zip(xy, xy[1:]))

# Elegant solution found on Reddit
sum(x < y for x, y in zip(data, data[1:]))
sum(x < y for x, y in zip(data, data[3:]))

# This part two solution is interesting because it only does a
# comparsion on data[0] and data[3]. If this solution is correct
# then that means if a < d then a + b + c < d + b + c.

# Let a, b, c, d ∈ 𝘕
# prove that a < d iff (a + b + c) < (d + b + c)
# proof by contradiction:
#  Assume
#        a < d ⇒ (a + b + c) > (d + b + c)
#        a < d ⇒ (a + b + c - b - c) > d
#        a < d ⇒ a > d
# QED

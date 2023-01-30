#!/usr/bin/env python
import itertools as it

with open("inputs/day01.txt", "r") as f:
    aoc_input = f.readlines()

split_input = it.groupby(aoc_input, lambda x: x == "\n")
total_cals = [sum(map(lambda x: int(x), group)) for k, group in split_input if not k]
ans01 = max(total_cals)
ans02 = sum(sorted(total_cals)[-3:])

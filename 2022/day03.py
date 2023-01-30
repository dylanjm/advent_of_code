#!/usr/bin/env python
import functools as ft
from string import ascii_lowercase as alc

with open("inputs/day03.txt", "r") as f:
    aoc_input = f.readlines()
    aoc_input = [aoc.replace("\n", "") for aoc in aoc_input]

compartments = [[set(i[:len(i)//2]), set(i[len(i)//2:])] for i in aoc_input]

ans_map = dict(zip(alc + alc.upper(), range(1,53)))

ans01 = sum([ans_map[(x[0] & x[1]).pop()] for x in compartments])

groups = list(zip(*[iter(aoc_input)]*3))

all_scores = []
for g in groups:
    grouped = [set(_) for _ in g]
    badge = ft.reduce(lambda x,y: x&y, grouped).pop()
    score = ans_map[badge]
    all_scores.append(score)

ans02 = sum(all_scores)

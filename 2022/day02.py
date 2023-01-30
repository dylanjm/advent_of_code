#!/usr/bin/env python

# A|X - Rock - 1 pts
# B|Y - Paper - 2 pts
# C|Z - Sissors - 3 pts

# Win - 6 pts
# Draw - 3 pts
# Lose - 0 pts

# AX - Draw - 4 pts
# AY - Win - 8 pts
# AZ - Lose - 3 pts
# BX - Lose - 1 pts
# BY - Draw - 5 pts
# BZ - Win - 9 pts
# CX - Win - 7 pts
# CY - Lose - 2 pts
# CZ - Draw - 6 pts

GAME = {
    "AX": 4,
    "AY": 8,
    "AZ": 3,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6
}

GAME02 = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 2,
    "CY": 6,
    "CZ": 7
}


with open("inputs/day02.txt", "r") as f:
    aoc_input = f.readlines()

aoc = list(map(lambda x: x.replace(' ', '').replace('\n',''), aoc_input))

ans01 = sum([GAME[i] for i in aoc])

ans02 = sum([GAME02[i] for i in aoc])

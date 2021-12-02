#!/usr/bin/env python3
from math import prod

def part_one():
    with open('inputs/input02.txt') as f:
        data = [(i.split(' ')[0], int(i.split(' ')[1]))  for i in f.readlines()]
    pos = (0, 0)
    for k, v  in data:
        if k == 'up':
            y = -v
            x = 0
        elif k == 'down':
            y = v
            x = 0
        else:
            y = 0
            x = v
        pos = (pos[0] + x, pos[1] + y)
    print(prod(pos))

def part_two():
    with open('inputs/input02.txt') as f:
        data = [(i.split(' ')[0], int(i.split(' ')[1]))  for i in f.readlines()]

    pos = (0, 0)
    aim = 0
    for k, v in data:
        if k == 'up':
            z = -v
            y = 0
            x = 0
        elif k == 'down':
            z = v
            y = 0
            x = 0
        else:
            z = 0
            y = aim * v
            x = v
        pos = (pos[0] + x, pos[1] + y)
        aim += z
    print(prod(pos))

# Here is an elegant solution from Reddit. It's cool because it leverages
# the new structural pattern matching feature in Python 3.10.0
# https://www.reddit.com/r/adventofcode/comments/r6zd93/2021_day_2_solutions/hmwbtbe/
def reddit_solution():
    h = d = a = 0
    for x in open('inputs/input02.txt'):
        match x.split():
            case 'forward', n:
                h += int(n)
                d += int(n)*a
            case 'up', n:
                a -= int(n)
            case 'down', n:
                a += int(n)
    print(h*a, h*d)


if __name__ == '__main__':
    part_one()
    part_two()
    reddit_solution()

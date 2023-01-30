#!/usr/bin/env python3
from typing import List
from collections import Counter

test = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

def make_ratings_generator(kind):
    rating_rules = {
        'o2': ('1', lambda x,y: x / y  >= 0.5, '0'),
        'co2':('0', lambda x,y: x / y <= 0.5, '1')
    }
    def gen(data):
        atom, pred, opatom = rating_rules[kind]
        max_size = len(data[0])
        for i in range(max_size):
            if len(data) == 1:
                break
            nums = [k[i] for k in data].count(atom)
            if pred(nums, len(data)):
                data = list(filter(lambda x: x[i] == atom, data))
            else:
                data = list(filter(lambda x: x[i] == opatom, data))
        return int(data[0], base=2)
    return gen

def compute_gamma(intervals, nums):
    zeros = ones = 0
    gamma = ''
    for a,b in intervals:
        for n in nums:
            if a <= n < b:
                ones += 1
            elif n > b:
                if ((n - b) % b) >= a:
                    ones += 1
                else:
                    zeros += 1
            else:
                zeros += 1
        gamma += '1' if ones > zeros else '0'
        zeros = ones = 0
    return gamma


def main():
    with open('inputs/input03.txt') as f:
        data = f.readlines()
        ###
        # Part One
        ###
        max_num = len(data[0])
        nums = [int(_, base=2) for _ in data]
        powers = [2**i for i in range(max_num)]
        intervals = list(zip(powers, powers[1:]))[::-1]
        gamma = compute_gamma(intervals, nums)
        epsilon = "".join([str(int(_)^1) for _ in gamma])
        gamma10 = int(gamma, base=2)
        epsilon10 = int(epsilon, base=2)
        ans = gamma10 * epsilon10
        print(f"Part 1:\n{gamma} = {gamma10}\n{epsilon} = {epsilon10}\n{gamma10} * {epsilon10} = {ans}\n")
        ###
        # Part Two
        ###
        o2 = make_ratings_generator('o2')
        co2 = make_ratings_generator('co2')
        print(f"Part 2:\n{o2(data) * co2(data)}\n")


# Very interesting solution found on reddit:
# https://www.reddit.com/r/adventofcode/comments/r7r0ff/2021_day_3_solutions/hn1wnae/?context=1
# I've made a few modifications to the original to make it run a bit better.
# Looking at this more in-depth... I have no clue how this code works.
# I get right answers for my input, but the test input is wrong.
def find(most) -> str:
    rows = open('inputs/input03.txt').read().split()
    for i in range(12):
        if len(rows) == 1:
            break
        c = Counter(r[i] for r in rows)
        rows = [
            r for r in rows
            if (r[i] == '1') != (c['1'] >= c['0']) ^ most
        ]
    return rows[0]


def reddit_solution():
    gamma = sum(
        2 ** (11 - i)
        for i, col in enumerate(zip(*open('inputs/input03.txt').read().split()))
        if sum(map(int, col)) > len(col) / 2
    )
    print('Reddit Solution:')
    print(gamma * (gamma ^ (2 ** 12 - 1)))
    print(int(find(True), 2) * int(find(False), 2))


if __name__ == '__main__':
    main()
    reddit_solution()

#!/usr/bin/env python3
import numpy as np

def main():

    n, *b = open('inputs/input04.txt')         # read input from stdin
    b = np.loadtxt(b, int).reshape(-1,5,5)     # load boards into 3D array

    for n in map(int, n.split(',')):           # loop over drawn numbers
        b[b == n] = -1                         # mark current number as -1
        m = (b == -1)                          # get all marked numbers
        win = (m.all(1) | m.all(2)).any(1)     # check for win condition
        if win.any():
            print((b * ~m)[win].sum() * n)     # print winning score
            b = b[~win]
    print(b)


if __name__ == '__main__':
    main()

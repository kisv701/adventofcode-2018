import re
from datetime import datetime

#This solution is slow, beware!

def pop_pair(s):
    prev_length = 99999999999

    while prev_length > len(s):
        prev_length = len(s)
        i = 1
        while i < len(s):
            u1 = s[i].upper()
            u2 = s[i - 1].upper()
            c1 = s[i]
            c2 = s[i - 1]
            if u1 == u2 and c1 != c2:
                s[i-1:i+1] = []

            i += 1
    return s

def puzzle_one(lines):
    print("December 5, First puzzle")
    s = list(lines[0])
    s = pop_pair(s)
    print("Reduced polymer length is {}".format(len(s)))

def puzzle_two(lines):
    print("December 5, Second puzzle")
    s = list(lines[0])
    chars = set([c.upper() for c in s])
    lowest_poly = 9999999999999
    for c in chars:
        s_temp = [x for x in s if x != c and x != c.lower()]
        s_temp = pop_pair(s_temp)
        if len(s_temp) < lowest_poly:
            lowest_poly = len(s_temp)
        print('{} gives a length of {}'.format(c, len(s_temp)))

    print("Lowest length polymer is {}".format(lowest_poly))


if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('inputs/day5.txt')]
    puzzle_one(lines)
    puzzle_two(lines)

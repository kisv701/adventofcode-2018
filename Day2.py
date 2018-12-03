from collections import Counter
# Day 2 AdventOfCode


def puzzle_one(lines):
    print("December 2, First puzzle")

    count_double, count_triple = 0, 0
    for line in lines:
        counts = list(Counter(line).values())
        count_double += int(2 in counts)
        count_triple += int(3 in counts)

    print("Doubles: {}, Triples: {}, Checksum: {}".format(count_double, count_triple, count_double*count_triple))


def puzzle_two(lines):
    print("December 2, Second puzzle")

    for i, s1 in enumerate(lines):
        for j in range(i, len(lines)):
            if is_correct_boxes(s1, lines[j]):
                common_chars = ''
                for k, _ in enumerate(s1):
                    if s1[k] == lines[j][k]:
                        common_chars += s1[k]
                print('Common chars: {}'.format(common_chars))
                return


def is_correct_boxes(s1, s2):
    miss_counter = 0
    for i in range(len(s1)):
        miss_counter += int(s1[i] != s2[i])
    return miss_counter == 1


if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('inputs/day2.txt')]
    puzzle_one(lines)
    puzzle_two(lines)

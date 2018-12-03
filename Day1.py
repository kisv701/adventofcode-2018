
# Day 1 AdventOfCode

def puzzle_one():
    print("December 1, First puzzle")
    lines = [int(line) for line in open('inputs/day1.txt')]
    print("The final frequency is {}. \n".format(sum(lines)))

def puzzle_two():
    print("December 1, Second puzzle")
    seq = [int(line) for line in open('inputs/day1.txt')]
    seen = set()
    current_freq, index = 0, 0

    while current_freq not in seen:
        seen.add(current_freq)
        current_freq += seq[index]
        index = (index+1) % len(seq)

    print("The first reappearing frequency is {}. \n".format(current_freq))


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()

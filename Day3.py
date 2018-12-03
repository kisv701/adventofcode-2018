import re


def parse_line(line):
    (id, x, y, size) = re.findall(r"[\w']+", line)
    (w, h) = size.split('x')
    return int(id), int(x), int(y), int(w), int(h)


# Make a dict where each 'ROWxCOL' is key for number of appearances of that coordinate
def pos_counter(lines):
    seen = dict()
    for line in lines:
        (_, x, y, w, h) = parse_line(line)

        for r in range(h):
            for c in range(w):
                s = str(x+c+1) + 'x' + str(y+r+1)
                if s in seen:
                    seen[s] += 1
                else:
                    seen[s] = 1
    return seen

def puzzle_one(lines):
    print("December 3, First puzzle")
    seen = pos_counter(lines)
    seen_twice = {k: v for k, v in seen.items() if v > 1}
    print("Square inches of double claimed fabric is {}".format(len(seen_twice)))

def puzzle_two(lines):
    print("December 3, Second puzzle")
    seen = pos_counter(lines)

    for line in lines:
        (id, x, y, w, h) = parse_line(line)
        found = True
        for r in range(h):
            for c in range(w):
                s = str(x+c+1) + 'x' + str(y+r+1)
                if s in seen:
                    if seen[s] > 1:
                        found = False
        if found:
            print("id of correct part {}".format(id))



if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('inputs/day3.txt')]
    puzzle_one(lines)
    puzzle_two(lines)

import re

class Sky():
    def __init__(self):
        self.stars = []
        self.update_counter = 0

    def insert(self, star):
        self.stars.append(star)

    def update(self):
        self.update_counter += 1
        for star in self.stars:
            star.update()

    def revert(self):
        self.update_counter -= 1
        for star in self.stars:
            star.revert()

    def spread(self):
        # min_x = min([star.x for star in self.stars])
        # max_x = max([star.x for star in self.stars])
        min_y = min([star.y for star in self.stars])
        max_y = max([star.y for star in self.stars])

        return max_y - min_y

    def __str__(self):
        min_x = min([star.x for star in self.stars])
        max_x = max([star.x for star in self.stars])
        min_y = min([star.y for star in self.stars])
        max_y = max([star.y for star in self.stars])
        rows = [[] for _ in range(max_y - min_y+1)]

        for star in self.stars:
            row = star.y - min_y
            rows[row].append(star.x - min_x)

        s = ''
        for row in rows:
            for col in range(max(row)+1):
                if col in row:
                    s += "#"
                else:
                    s += "."
            s += '\n'
        return s

class Star():
    def __init__(self, line):
        [self.x, self.y, self.dx, self.dy] = [int(x) for x in re.findall('[-]?\d+', line)]


    def update(self):
        self.x += self.dx
        self.y += self.dy

    def revert(self):
        self.x -= self.dx
        self.y -= self.dy

    def __str__(self):
        "x: {}, y: {}, dx: {}, dy: {}".format(self.x, self.y, self.dx, self.dy)


def puzzle(lines):
    print("December 10, Puzzle")

    sky = Sky()
    for line in lines:
        star = Star(line)
        sky.insert(star)


    spread = sky.spread() + 1
    while spread >= sky.spread():
        spread = sky.spread()
        sky.update()


    sky.revert()
    print(sky)
    print("T: {}s".format(sky.update_counter))

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('inputs/day10.txt')]

    puzzle(lines)
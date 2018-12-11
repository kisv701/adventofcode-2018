import numpy as np
def mh(p1, p2):
    return abs(p1['x']-p2['x']) + abs(p1['y']-p2['y'])

def puzzle_one(lines):
    print("December 6, First puzzle")
    points = []
    for line in lines:
        [x, y] = line.split(',')
        x = int(x)
        y = int(y)
        points.append({
            "x": x,
            "y": y
        })

    min_x = min([p['x'] for p in points])
    min_y = min([p['y'] for p in points])
    max_x = max([p['x'] for p in points])
    max_y = max([p['y'] for p in points])


    print("X: {} - {}, Y: {} - {}".format(min_x, max_x, min_y, max_y))

    counter = [0 for _ in range(0, len(points))]

    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            current_point = {'x': x, 'y': y}
            mandist = [mh(current_point, p) for p in points]
            min_dist = sorted(mandist)
            if min_dist[0] != min_dist[1]:
                if x == min_x or x == max_x or y == min_y or y == max_y:
                    counter[mandist.index(min(mandist))] = -100000000000
                else:
                    counter[mandist.index(min(mandist))] += 1

    print(max(counter))

def puzzle_two(lines):
    print("December 6, Second puzzle")
    points = []
    for line in lines:
        [x, y] = line.split(',')
        x = int(x)
        y = int(y)
        points.append({
            "x": x,
            "y": y
        })

    min_x = min([p['x'] for p in points])
    min_y = min([p['y'] for p in points])
    max_x = max([p['x'] for p in points])
    max_y = max([p['y'] for p in points])


    print("X: {} - {}, Y: {} - {}".format(min_x, max_x, min_y, max_y))

    counter = 0

    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            current_point = {'x': x, 'y': y}
            mandist = sum([mh(current_point, p) for p in points])
            if mandist < 10000:
                counter += 1
    print(counter)


if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('inputs/day6.txt')]
    # lines = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
    puzzle_one(lines)
    puzzle_two(lines)
class Circle():
    def __init__(self):
        self.arr = [0]
        self.current = 0

    def insert(self, marble):
        self.step_clockwise()
        self.arr.insert(self.current, marble)

    def remove(self):
        self.step_counter_clockwise()
        marble = self.arr.pop(self.current)
        self.current %= len(self.arr)
        return marble

    def step_clockwise(self):
        self.current += 2
        self.current %= len(self.arr)

    def step_counter_clockwise(self):
        self.current -= 7
        self.current %= len(self.arr)


def puzzle_one(data):
    print("December 9, First puzzle")
    players = [0 for _ in range(data[0])]
    player = 0
    marbles = data[1]
    circle = Circle()

    for marble in range(1, marbles+1):

        if marble % 23 == 0:
            players[player] += marble
            players[player] += circle.remove()
        else:
            circle.insert(marble)

        player += 1
        player %= len(players)
    print('{} wins with {} points'.format(players.index(max(players)) + 1, max(players)))


def puzzle_two(lines):
    print("December 9, Second puzzle")


if __name__ == '__main__':
    data = [(9, 25), (10, 1618), (13, 7999), (17, 1104), (21, 6111), (30, 5807), (446, 71522*100)]
    puzzle_one(data[-1])
    puzzle_two(data)


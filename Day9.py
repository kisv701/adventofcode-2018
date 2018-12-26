class MarbleMania:
    def __init__(self, players):
        self.array = []
        self.pointer = 0
        self.array.append(0)
        self.players = [0 for _ in range(players)]

    def clockwise(self):
        self.pointer += 2
        if self.pointer <= 1:
            self.pointer = len(self.array) + self.pointer
        if self.pointer > len(self.array):
            self.pointer = self.pointer - len(self.array)

    def pop_seven(self):
        self.pointer -= 7
        if self.pointer < 1:
            self.pointer = len(self.array) + self.pointer
        if self.pointer > len(self.array):
            self.pointer = self.pointer - len(self.array)
        return self.array.pop(self.pointer)

    def add(self, other, player):
        if other % 23 == 0:
            self.collect(player)
            return

        if len(self.array) == 1:
            self.pointer = 1
        else:
            self.clockwise()
        self.array.insert(self.pointer, other)

    def collect(self, player):
        v = self.pop_seven()
        v += 23
        self.players[player-1] += v

    def __str__(self):
        s = ''
        for idx, marble in enumerate(self.array):
            if idx == self.pointer:
                s += '({})'.format(marble)
            else:
                s += ' {} '.format(marble)

        return s

def puzzle_one(lines):
    print("December 9, First puzzle")
    players = 446
    marbles = 71522
    current_player = 0
    game = MarbleMania(players)
    for marble in range(1, marbles+1):
        current_player = current_player % players + 1
        game.add(marble, current_player)
        # print(current_player, marble, '|', game)
    print(max(game.players))


def puzzle_two(lines):
    print("December 9, Second puzzle")


if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('inputs/day9.txt')]
    puzzle_one(lines)
    puzzle_two(lines)

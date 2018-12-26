class Node():
    def __init__(self):
        self.children = []
        self.metadata = []
        self.id = -1

    def add_child(self, child):
        self.children.append(child)

    def sum_meta(self):
        v = 0
        for data in self.metadata:
            v += data
        return v


def parse_input(entries, pointer):
    node = Node()
    children_count = entries[pointer]
    metadata_count = entries[pointer + 1]
    pointer += 2
    for i in range(children_count):
        (child, pointer) = parse_input(entries, pointer)
        node.add_child(child)

    node.metadata = entries[pointer:pointer+metadata_count]
    pointer += metadata_count

    return node, pointer


def calc_sum_meta(node):
    s = node.sum_meta()
    for c in node.children:
        s += calc_sum_meta(c)
    return s


def calc_value_node(node):
    if len(node.children) < 1:
        return node.sum_meta()

    v = 0
    for idx in node.metadata:
        idx -= 1
        if idx < len(node.children):
            v += calc_value_node(node.children[idx])
    return v


def puzzle_one(lines):
    print("December 8, First puzzle")
    entries = [int(x) for x in lines[0].split(' ')]
    root, pointer = parse_input(entries, 0)
    print(calc_sum_meta(root))


def puzzle_two(lines):
    print("December 8, Second puzzle")
    entries = [int(x) for x in lines[0].split(' ')]
    root, pointer = parse_input(entries, 0)
    print(calc_value_node(root))

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('inputs/day8.txt')]
    #lines = ['2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2']
    puzzle_one(lines)
    puzzle_two(lines)

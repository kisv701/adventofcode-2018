def parseInput(lines):
    tasks = set()
    pre_req = dict()
    for line in lines:
        pre = line[5]
        task = line[36]

        if task in pre_req:
            pre_req[task].append(pre)
        else:
            pre_req[task] = [pre]

        tasks.add(pre)
        tasks.add(task)

    tasks = sorted(list(tasks))
    return (tasks, pre_req)

def update_blocking(blocking, tasks, completed_tasks):
    for current_task in completed_tasks:
        for task in tasks:
            if task in blocking and current_task in blocking[task]:
                blocking[task].remove(current_task)
                if len(blocking[task]) < 1:
                    del blocking[task]
    return blocking

def update_workers(workers):
    for i in range(len(workers)):
        workers[i][0] = max(workers[i][0] - 1, 0)
    return workers

def task_time(task):
    return ord(task) - 4


def puzzle_one(lines):
    print("December 7, First puzzle")
    seq = []
    tasks, blocking = parseInput(lines)

    while len(seq) < len(tasks):
        ready = [x for x in tasks if x not in blocking and x not in seq]

        current_task = ready[0]
        blocking = update_blocking(blocking, tasks, [current_task])
        seq.append(current_task)

    print(''.join(seq))  # IJLFUVDACEHGRZPNKQWSBTMXOY

def puzzle_two(lines):
    print("December 7, Second puzzle")
    seq = []
    workers = [[0, None], [0, None], [0, None], [0, None], [0, None]]
    tasks, blocking = parseInput(lines)
    active_tasks = []
    while len(seq) < len(tasks):
        ready = [x for x in tasks if x not in blocking and x not in seq and x not in active_tasks]
        for current_task in ready:
            for i in range(len(workers)):
                if workers[i][1] is None:
                    workers[i] = [task_time(current_task), current_task]
                    active_tasks.append(current_task)
                    break

        completed_tasks = [x for (time, x) in workers if time == 0 and x is not None]
        blocking = update_blocking(blocking, tasks, completed_tasks)
        for completed_task in completed_tasks:
            seq.append(completed_task)

        for i in range(len(workers)):
            if workers[i][1] in completed_tasks:
                workers[i][1] = None

        update_workers(workers)
    print(''.join(seq))


if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('inputs/day7.txt')]
    lines = ['Step C must be finished before step A can begin.', 'Step C must be finished before step F can begin.',
             'Step A must be finished before step B can begin.', 'Step A must be finished before step D can begin.',
             'Step B must be finished before step E can begin.', 'Step D must be finished before step E can begin.',
             'Step F must be finished before step E can begin.']
    puzzle_one(lines)
    puzzle_two(lines)

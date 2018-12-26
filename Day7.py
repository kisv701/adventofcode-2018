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

def getActiveTasks(workers):
    out = []
    for worker in workers:
        if worker.task is not None:
            out.append(worker.task)
    return out

def task_time(task):
    return ord(task) - 4

class Worker():
    def __init__(self):
        self.task = None
        self.time = 0

    def step(self):
        self.time = max(self.time - 1, 0)
        if self.time == 0:
            completed = self.task
            self.task = None
            return completed

    def isReady(self):
        return self.time == 0

    def setTask(self, task):
        self.task = task
        self.time = ord(task) - 4

    def __str__(self):
        return "{}:{}".format(self.task, self.time)


def puzzle_one(lines):
    print("December 7, First puzzle")
    seq = []
    tasks, pre_req = parseInput(lines)

    while len(seq) < len(tasks):
        ready = [x for x in tasks if x not in blocking and x not in seq]

        current_task = ready[0]
        blocking = update_blocking(blocking, tasks, [current_task])
        seq.append(current_task)

    print(''.join(seq))  # IJLFUVDACEHGRZPNKQWSBTMXOY

def puzzle_two(lines):
    print("December 7, Second puzzle")
    seq = []
    workers = [Worker() for _ in range(5)]
    tasks, blocking = parseInput(lines)

    t = 0
    while len(seq) < len(tasks):

        # Find ready tasks
        ready = [x for x in tasks if x not in blocking and x not in seq and x not in getActiveTasks(workers)]

        # Assign workers
        for current_task in ready:
            for worker in workers:
                if worker.isReady():
                    worker.setTask(current_task)
                    break

        # Take step in time
        finished_tasks = []
        for worker in workers:
            step_out = worker.step()
            if step_out is not None:
                finished_tasks.append(step_out)
        t += 1

        # Check if some task is finished
        for finished_task in finished_tasks:
                seq.append(finished_task)
                update_blocking(blocking, tasks, seq)
        print("{}: {}, {}, {}, {}, {}".format(t, workers[0], workers[1], workers[2], workers[3], workers[4]))

    print(t)
    print(''.join(seq))


if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('inputs/day7.txt')]
    # lines = ['Step C must be finished before step A can begin.', 'Step C must be finished before step F can begin.',
    #          'Step A must be finished before step B can begin.', 'Step A must be finished before step D can begin.',
    #          'Step B must be finished before step E can begin.', 'Step D must be finished before step E can begin.',
    #          'Step F must be finished before step E can begin.']
    # puzzle_one(lines)
    puzzle_two(lines)

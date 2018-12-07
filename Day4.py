import re
from datetime import datetime



def puzzle_one(lines):
    print("December 4, First puzzle")

    timestamps = []
    events = []
    guards = dict()

    for line in lines:
        datetime_object = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
        text = line[19:]
        guard_id = re.findall(r'\d+', text)
        if guard_id:
            guards[guard_id[0]] = [0 for _ in range(60)]
        timestamps.append(datetime_object)
        events.append(text)

    events = [x for _, x in sorted(zip(timestamps, events))]
    timestamps.sort()

    current_guard = -1

    for i, event in enumerate(events):
        guard_id = re.findall(r'\d+', event)

        if guard_id:
            current_guard = guard_id[0]
        elif event == 'falls asleep':
            start = timestamps[i].minute
            stop = timestamps[i+1].minute
            for j in range(start, stop):
                guards[current_guard][j] += 1

    max_sleep = 0
    max_guard = 0
    best_minute = -1
    for guard, counter in guards.items():
        sleep = sum(counter)
        if sleep > max_sleep:
            max_sleep = sleep
            max_guard = guard
            best_minute = counter.index(max(counter))
    print(int(max_guard)*int(best_minute))


def puzzle_two(lines):
    print("December 4, Second puzzle")

    timestamps = []
    events = []
    guards = dict()

    for line in lines:
        datetime_object = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
        text = line[19:]
        guard_id = re.findall(r'\d+', text)
        if guard_id:
            guards[guard_id[0]] = [0 for _ in range(60)]
        timestamps.append(datetime_object)
        events.append(text)

    events = [x for _, x in sorted(zip(timestamps, events))]
    timestamps.sort()

    current_guard = -1

    for i, event in enumerate(events):
        guard_id = re.findall(r'\d+', event)

        if guard_id:
            current_guard = guard_id[0]
        elif event == 'falls asleep':
            start = timestamps[i].minute
            stop = timestamps[i+1].minute
            for j in range(start, stop):
                guards[current_guard][j] += 1

    max_sleep = 0
    max_guard = 0
    best_minute = -1
    for guard, counter in guards.items():
        sleep = max(counter)
        if sleep > max_sleep:
            max_sleep = sleep
            max_guard = guard
            best_minute = counter.index(max(counter))
    print(int(max_guard)*int(best_minute))

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('inputs/day4.txt')]
    puzzle_one(lines)
    puzzle_two(lines)

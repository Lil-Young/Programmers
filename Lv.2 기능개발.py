from math import ceil
from collections import deque


def solution(progresses, speeds):
    long_day = 0
    answer = []
    days = deque(ceil((100 - p) / s) for p, s in zip(progresses, speeds))
    print(days)
    while days:
        day = days.popleft()
        print(day)
        if day > long_day:
            answer.append(1)
            long_day = day
        else:
            answer[-1] += 1

    return answer

if __name__ == '__main__':
    #result = solution([93, 30, 55], [1, 30, 5])
    result1 = solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
    #print(result)
    print(result1)
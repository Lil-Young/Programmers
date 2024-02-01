def solution(n:int, lost:list, reserve:list):
    reserve.sort()
    new_lost = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            new_lost.append(i)
    new_lost.sort()
    answer = n - len(new_lost)
    for i in new_lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
    return answer

if __name__ == "__main__":
    result = solution(6, [3, 4, 5], [3, 4, 6])
    print(result)
def solution(n):
    answer = 1
    cnt, sum = 1, 0
    start, end = 0, n
    _list = [x for x in range(1, n+1)]
    for i in range(n//2):
        for j in range(n//2 + 1):
            sum += _list[start]
            start+=1
            if sum == n:
                answer+=1
                break
        sum = 0
        start = 0
        
        return answer


if __name__ == "__main__":
    result = solution(15)
    print(result)
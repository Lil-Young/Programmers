def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        v = max(i//n, i%n) + 1
        answer.append(v)
    return answer

if __name__ == '__main__':
    result = solution(4, 7, 14)
    print(result)

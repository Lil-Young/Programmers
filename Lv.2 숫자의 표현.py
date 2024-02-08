def solution(n):
    answer = 0
    cnt, sum = 1, 0
    while cnt <= n:
        sum = 0
        for i in range(cnt, n+1):
            sum += i
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
        cnt += 1
    return answer


if __name__ == "__main__":
    result = solution(15)
    print(result)
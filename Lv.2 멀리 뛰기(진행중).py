def solution(n):
    cnt = 2
    if n == 1:
        return 1
    for i in range(1, n-1):
        cnt += i
    return cnt

# DP 공부하고 풀기


if __name__ == "__main__":
    result = solution(2000)
    print(result)
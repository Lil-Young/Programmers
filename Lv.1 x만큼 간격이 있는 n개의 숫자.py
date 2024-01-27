def solution(x, n):
    if x > 0:
        answer = [x for x in range(x, x*n+1, x)]
    elif x == 0:
        answer = [0] * n
    else: 
        answer = [x for x in range(x, x*n-1, x)]
    return answer

if __name__ == "__main__":
    result = solution(0, 2)
    print(result)
def solution(n):
    for i in range(0, 500):
        if n%2 == 0:
            n = n//2
        elif n == 1:
            return i
        else:
            n = n*3+1
    return -1

if __name__ == "__main__":
    result = solution(626331)
    print(result)
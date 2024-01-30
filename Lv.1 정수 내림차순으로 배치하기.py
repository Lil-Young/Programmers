def solution(n):
    a = sorted(str(n), reverse=True)
    return int(''.join(a))

if __name__ == "__main__":
    result = solution(118372)
    print(result)
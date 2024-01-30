def solution(n):
    a = n**0.5
    return pow(int(a)+1, 2) if a%1 == 0 else -1

if __name__ == "__main__":
    result = solution(3)
    print(result)
    
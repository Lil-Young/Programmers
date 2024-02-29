def solution(n):
    a, b = 1, 2
    if n == 1:
        return 1
    for _ in range(2, n):
        a, b = b, a+b
    
    return b%1234567

if __name__ == "__main__":
    result = solution(2)
    print(result)
def solution(a, b):
    if a < b:
        return sum([i for i in range(a, b+1)])
    elif a > b:
        return sum([i for i in range(a, b-1, -1)])
    else:
        return a

if __name__ == "__main__":
    result = solution(3, 3)
    print(result)
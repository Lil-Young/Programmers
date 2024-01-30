def solution(x):
    x_list = list(map(int, list(str(x))))
    return x%sum(x_list) == 0

if __name__ == "__main__":
    result = solution(18)
    print(result)
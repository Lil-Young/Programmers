def solution(n):
    num = 1
    _list = []
    while num <= n:
        if n%num == 0:
            _list.append(num)
        num += 1
    return sum(_list)

if __name__ == "__main__":
    result = solution(5)
    print(result)
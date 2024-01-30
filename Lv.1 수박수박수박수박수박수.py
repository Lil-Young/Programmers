def solution(n):
    _str = ""
    for i in range(n):
        _str+="수" if i%2 == 0 else "박"
    return _str

if __name__ == "__main__":
    result = solution(3)
    print(result)
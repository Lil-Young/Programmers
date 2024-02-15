def solution(s):
    _list = []
    for i in s:
        if i == '(':
            _list.append('(')
        else:
            try:
                _list.pop()
            except:
                return False
    return len(_list) == 0

if __name__ == "__main__":
    result = solution("())(")
    print(result)
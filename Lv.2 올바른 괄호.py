def solution(s):
    answer = True
    _list = []
    for i in s:
        if len(_list) == 0 and i == ')':
            return False
        _list.append(i)
        if _list.count('(') == _list.count(')'):
            _list.clear()
    
    return len(_list) == 0

if __name__ == "__main__":
    result = solution("(())()")
    print(result)
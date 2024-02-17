from math import sqrt
def solution(brown, yellow):
    answer = []
    _list = []
    val = brown + yellow
    if val % 2 == 0 or sqrt(val)*10 != 0: # 짝수
        for y in range(3, val//2):
            x = val//y
            if val%y == 0:
                a = sorted([x,y], reverse=True)
                if a not in _list:
                    _list.append(a)
        for i in _list:
            if i[0] >= i[1]:
                x = i[0] - 2
                y = i[1] - 2
                if yellow == x*y:
                    return i
    else:
        x = x = int(sqrt(val))
        if x*10 != 0:
            x = int((sqrt(val) + (sqrt(val) - int(sqrt(val)) + 0.5)))
            y = int(sqrt(val))
            return [x, y]
        x = int(sqrt(val))
        y = int(sqrt(val))
        return [x, y]

if __name__ == "__main__":
    result = solution(24, 9)
    print(result)
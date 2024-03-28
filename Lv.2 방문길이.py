def solution(dirs:str):
    answer = 0
    x, y = 5, 5
    min_num, max_num = 0, 10
    location = []
    # U: x+1 / D: x-1 / R: y+1 / L: y-1
    for i in dirs:
        if i == 'U' and x+1 <= max_num:
            loc = sorted([(x, y), (x+1, y)])
            if loc not in location:
                location.append(loc)
                answer += 1
            x += 1
        elif i == 'D' and x-1 >= min_num:
            loc = sorted([(x, y), (x-1, y)])
            if loc not in location:
                location.append(loc)
                answer += 1
            x -= 1
        elif i == 'R' and y+1 <= max_num:
            loc = sorted([(x, y), (x, y+1)])
            if loc not in location:
                location.append(loc)
                answer += 1
            y += 1
        elif i == 'L' and y-1 >= min_num:
            loc = sorted([(x, y), (x, y-1)])
            if loc not in location:
                location.append(loc)
                answer += 1
            y -= 1
        else:
            continue

    return answer

if __name__ == '__main__':
    result = solution("ULURRDLLU")
    print(result)
    result2 = solution("LULLLLLLU")
    print(result2)
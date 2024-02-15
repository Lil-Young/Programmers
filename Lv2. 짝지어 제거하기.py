def solution(s):
    s = list(s)
    answer = -1
    cnt = 0
    pos1, pos2 = 0, 2
    for _ in range(len(s)-1):
        if len(s) == 0:
            break
        if s[pos1:pos2][0] == s[pos1:pos2][1]:
            print(s[pos1:pos2])
            del s[pos1:pos2]
            pos1, pos2 = 0, 2
            continue
        pos1 += 1
        pos2 += 1
    answer = 1 if len(s) == 0 else 0
    return answer

if __name__ == "__main__":
    result = solution("baabaa")
    print(result)
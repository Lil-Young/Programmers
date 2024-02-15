def solution(s):
    cnt_0, cnt_c = 0, 0
    while s != "1":
        cnt_0 += s.count('0')
        s_len = bin((s.count('1')))
        s = s_len[2:]
        cnt_c += 1
    return [cnt_c, cnt_0]

if __name__ == "__main__":
    result = solution("110010101001")
    print(result)
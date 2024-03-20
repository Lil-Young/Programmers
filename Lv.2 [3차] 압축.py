def solution(msg):
    answer = []
    n_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    now_number = 26
    n = len(list(msg))
    start, end = 0, 2
    while end <= n:
        if msg[start:end] not in n_dict:
            print(msg[start:end])
            now_number += 1
            n_dict[msg[start:end]] = now_number
            answer.append(n_dict[msg[start:end-1]])
            start = end - 1
            end = start + 2
        else:
            end += 1
    answer.append(n_dict[msg[start:end-1]])
    return answer

# 실행 과정
'''
msg = "KAKAO"
1. start 0, end 2
msg[0:2] = "KA"
now_number = 27
n_dict["KA"] = 27
answer.append(n_dict['K']), answer = [11]
2. start 1, end 3
msg[1:3] = "AK"
now_number = 28
n_dict["AK"] = 28
answer.append(n_dict['A']), answer = [11, 1]
3. start 2, end 4
msg[2:4] = "KA"
end += 1
start 2, end 5
msg[2:5] = "KAO"
now_number = 29
n_dict["KAO"] = 29
answer.append(n_dict['KA']), answer = [11, 1, 27]
4. start 4, end 6
end > "KAKAO 길이" -> while문 탈출
answer.append(n_dict[msg[start:end-1]]), answer.append(n_dict['O']), answer = [11, 1, 27, 15]
'''

if __name__ == '__main__':
    result = solution("KAKAO")
    print(result)

    # result1 = solution("TOBEORNOTTOBEORTOBEORNOT")
    # print(result1)

    # result2 = solution("ABABABABABABABAB")
    # print(result2)
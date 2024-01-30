def solution(s:str):
    answer = []
    s_list = s.split(" ")
    for i in range(len(s_list)):
        temp = ''
        for j in range(len(s_list[i])):
            if j%2 == 0:
                temp += s_list[i][j].upper()
            else:
                temp += s_list[i][j].lower()
        answer.append(temp)
    return ' '.join(answer)

def solution2(s:str):
    answer = ''
    s_list = s.split(" ")
    for i in range(len(s_list)):
        for j in range(len(s_list[i])):
            if j%2 == 0:
                answer += s_list[i][j].upper()
            else:
                answer += s_list[i][j].lower()
        answer += " "
    return answer

if __name__ == '__main__':
    test_string = 'K A    a cdcc    '
    result1 = solution(test_string)
    result2 = solution2(test_string)
    print(result1 == result2)
    print(result1, len(result1))
    print(result2, len(result2))
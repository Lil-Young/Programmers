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

if __name__ == '__main__':
    test_string = '  a  b  '
    result = solution(test_string)
    print(result)
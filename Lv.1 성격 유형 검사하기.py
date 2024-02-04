def solution(survey, choices):
    answer = ''
    # R, T / C, F / J, M / A, N
    _dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    # 각 문항의 점수를 해당 성격에 추가
    for idx, i in enumerate(survey):
        if choices[idx] == 1 or choices[idx] == 7:
            val = 3
        elif choices[idx] == 2 or choices[idx] == 6:
            val = 2
        elif choices[idx] == 3 or choices[idx] == 5:
            val = 1
        else:
            val = 0
        temp = i[0] if choices[idx] == 1 or choices[idx] == 2 or choices[idx] == 3 else i[1]
        _dict[temp] += val
    # 비교 후 answer에 추가
    answer += 'R' if _dict['R'] >= _dict['T'] else 'T'
    answer += 'C' if _dict['C'] >= _dict['F'] else 'F'
    answer += 'J' if _dict['J'] >= _dict['M'] else 'M'
    answer += 'A' if _dict['A'] >= _dict['N'] else 'N'
    return answer

if __name__ == "__main__":
    result = solution(["TR", "RT", "TR"], [7, 1, 3])
    print(result)
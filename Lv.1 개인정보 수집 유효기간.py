def solution(today, terms, privacies):
    answer = []
    _dict = {}
    # 약관 종류, 유효기간을 딕셔너리에 추가
    for i in terms:
        _type, _term = i.split(' ')
        _dict[_type] = _term
    # 오늘 날짜와 입력받은 날짜를 모두 일(day)로 바꾸고 그 둘을 비교하여 파기해야되는 개인정보를 answer에 추가
    # year -> month: year*12 + month
    # month -> day: month * 28 + day
    for idx, j in enumerate(privacies, start=1):
        day1 = (int(today[:4])*12+int(today[5:7]))*28+int(today[8:10])
        day2 = (int(j[:4])*12+int(j[5:7]))*28+int(j[8:10])
        if day1-day2 > int(_dict[j[-1]]) * 28 - 1:
            answer.append(idx)
    return answer

if __name__ == "__main__":
    result = solution("2020.01.01", 
                      ["Z 3", "D 5"],
                      ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
    print(result)
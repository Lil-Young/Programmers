import math

def solution(fees:list, records:list):
    # fees: 주차요금(기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)), records: 자동차의 입/출차 내역
    answer = []

    # 리스트 안에 문자열을 리스트로 만들고 차 번호를 기준으로 정렬
    records = sorted([x.split(' ') for x in records], key = lambda x:(x[1], x))
    # set을 이용해 차 번호 중복 제거 및 리스트 변환 후 오름차순 정렬
    set_r = sorted(list(set(x[1] for x in records)))
    # 차번호:이용시간 딕셔너리 생성
    cars_minute = {x:0 for x in set_r}
    # OUT을 안한 차의 시간 계산을 위함
    v = 23*60 + 59

    # 'IN'이면 stack에 넣고, 'OUT'이면 stack에서 뺀다.
    stack = []
    for i in records:
        to_minute = int(i[0][:2])*60 + int(i[0][3:])
        if stack and i[2] == "IN":
            pre_val = stack.pop()
            cars_minute[pre_val[1]] += (v - pre_val[0])

            stack.append((to_minute, i[1]))
            continue

        if i[2] == "IN":
            stack.append((to_minute, i[1]))
        elif i[2] == "OUT":
            pre_val = stack.pop()
            cars_minute[pre_val[1]] += (to_minute - pre_val[0])
    if stack:
        pre_val = stack.pop()
        cars_minute[pre_val[1]] += (v - pre_val[0])
    for i in cars_minute.values():
        fee = fees[1] + math.ceil((i - fees[0])/fees[2]) * fees[3]
        if fee > fees[1]:
            answer.append(fee)
        else:
            answer.append(fees[1])
    return answer

# 0000 | 34 + 300 = 334	| 5000 + ⌈(334 - 180) / 10⌉ x 600 = 14600

if __name__ == '__main__':
    result = solution([180, 5000, 10, 600],
                      ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
    print(result)
    result2 = solution([120, 0, 60, 591],
                       ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
    print(result2)
    result3 = solution([1, 461, 1, 10],
                       ["00:00 1234 IN"])
    print(result3)
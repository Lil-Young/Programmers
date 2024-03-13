def solution(priorities, location):
    answer = 0
    # return 하는 location은 1부터 시작
    # 우선순위가 높은 값부터 차례대로 큐에 넣기
    a = [x for x in range(1, len(priorities)+1)] # 우선순위에 해당이 되는 고유 값
    poi_dict = {}
    for x, y in zip(a, priorities):
        poi_dict[x] = y

    # priorities가 높은 순서대로 정렬
    sort_s = sorted(priorities, reverse=True)
    l = []
    idx = 0
    # 우선순위가 높은 순서대로 (고유값, 우선순위)를 l에 넣기
    while True:
        for n in poi_dict.items():
            if idx == len(sort_s):
                break
            if sort_s[idx] == n[1]:
                l.append(n)
                idx+=1
        if idx == len(sort_s):
            break
    # 찾으려고 하는 위치의 고유값을 loc에 넣기
    loc = list(poi_dict.items())[location][0]
    # 고유값의 위치 찾기
    for idx, i in enumerate(l):
        if i[0] == loc:
            return idx+1 
    return answer

if __name__ == '__main__':
    result1 = solution([2, 1, 3, 2], 2)
    result2 = solution([1, 1, 9, 1, 1, 1], 0)
    print(result1)
    print(result2)
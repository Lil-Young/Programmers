def solution(cacheSize:int, cities:list):
    # 캐시 크기가 0이면 모든 경우가 miss이므로 cities 길이의 5를 곱한 값을 return한다.
    if cacheSize == 0:
        return len(cities)*5
    
    # 리스트에 있는 도시들의 이름은 대소문자를 구분하지 않으므로 구분을 하기위해 전부 대문자로 바꿔준다.
    cities = [x.upper() for x in cities]

    answer = 0

    # LRU를 하기전에 먼저 새로운 리스트에 도시들의 이름을 넣는다. 
    a: list = []
    for idx, i in enumerate(cities):
        if i in a:
            a.remove(i)
            answer += 1
        else:
            answer += 5
        a.append(i)
        if len(a) == cacheSize:
            break

    # 빈 리스트에 넣으면서 입력받은 리스트를 다 돌았으면 answer을 return한다.
    if idx+1 == len(cities):
        return answer
    # 리스트들 다 안돌았으면 접근하지 않은 리스트부터 끝까지 LRU를 하기위해 새로운 리스트를 만든다.
    cities = cities[idx+1:]
    # LRU 과정
    for i in cities:
        if i in a:
            a.remove(i)
            a.append(i)
            answer+=1
        else:
            a.append(i)
            a.pop(0)
            answer+=5
    return answer

if __name__ == '__main__':
    result = solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
    print(result)
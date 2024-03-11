def solution(cacheSize:int, cities:list):
    print(cities)
    # if cacheSize == 0:
    #     return len(cities)*5
    # cities = [x.upper() for x in cities]
    # answer = 0
    # a: list = []
    # for idx, i in enumerate(cities):
    #     if i in a:
    #         a.remove(i)
    #         answer += 1
    #     else:
    #         answer += 5
    #     a.append(i)
    #     if len(a) == cacheSize:
    #         break
    # if idx+1 == len(cities):
    #     return answer
    # cities = cities[idx+1:]
    # for i in cities:
    #     if i in a:
    #         a.remove(i)
    #         a.append(i)
    #         answer+=1
    #     else:
    #         a.append(i)
    #         a.pop(0)
    #         answer+=5
    # return answer

if __name__ == '__main__':
    result = solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
    print(result)
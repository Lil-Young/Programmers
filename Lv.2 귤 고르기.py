from collections import Counter
def solution(k:str, tangerine:list):
    answer = 0
    a = list(set(tangerine))

    # k보다 큰 귤의 수 제외하기
    # Counter 패키지 사용하여 귤의 갯수 정렬하기
    cnt = Counter(tangerine)
    cnt = sorted(cnt.values(), reverse=True)

    ## 리스트 컴프리헨션을 사용하여 귤의 갯수 정렬하기
    # cnt = [tangerine.count(x) for x in a]
    # cnt.sort(reverse=True)

    ## dict의 values로 귤의 갯수 정렬하기
    # _dict = {}
    # for i in range(len(a)):
    #     _dict[a[i]] = tangerine.count(a[i])
    # cnt = list(_dict.values())
    # cnt.sort(reverse=True)
    total = 0

    for i in cnt:
        total += i
        answer += 1
        if total >= k:
            break
    
    return answer

# 7 5 3 3 / 6
if __name__ == "__main__":
    result = solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
    print(result)
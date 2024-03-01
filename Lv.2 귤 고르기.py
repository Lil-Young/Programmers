from collections import Counter
def solution(k:str, tangerine:list):
    answer = 0

    # k보다 큰 귤의 수 제외하기
    # Counter 패키지 사용하여 귤의 갯수 정렬하기
    cnt = Counter(tangerine)
    cnt = sorted(cnt.values(), reverse=True)

    total = 0

    for i in cnt:
        total += i
        answer += 1
        if total >= k:
            break
    
    return answer

if __name__ == "__main__":
    result = solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
    print(result)
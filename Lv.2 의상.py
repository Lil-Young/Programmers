def solution(clothes:list):
    answer = 1
    clodict = {}
    # 옷 종류마다 개수를 0으로 초기화
    for i in clothes:
        clodict[i[-1]] = 0

    # 옷 종류마다 개수 구하기
    for k in clothes:
        clodict[k[-1]] += len(k[:-1])
    
    # 옷 종류로 만들 수 있는 경우의 수 구하기
    for h in clodict.values():
        answer = (h+1)*answer

    # 아무 옷도 안입는 경우의 수 제외
    return answer-1

if __name__ == '__main__':
    result = solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
    print(result)
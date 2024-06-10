def solution(prices):
    answer = []
    for idx, price in enumerate(prices):
        a = 0
        for i in range(idx+1, len(prices)):
            a+=1
            if price > prices[i]:
                break
        answer.append(a)
    return answer


result = solution([1,2,3,2,3])
print(result)
from collections import Counter
def solution(want:list, number:list, discount:list):
    answer = 0
    cpy_discount = discount
    num = sum(number)
    for i in range(len(discount)):
        discount = cpy_discount[i:i+10]
        if len(discount) < num:
            break

        a = dict(Counter(discount))
        cnt = 0

        for idx, k in enumerate(want):
            try:
                if a[k] >= number[idx]:
                    cnt+=1
            except:
                break
        if cnt == len(want):
            answer += 1
        
    return answer

if __name__ == '__main__':
    result = solution(["banana", "apple", "rice", "pork", "pot"], 
                      [3, 2, 2, 2, 1], 
                      ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
                      )
    print(result)
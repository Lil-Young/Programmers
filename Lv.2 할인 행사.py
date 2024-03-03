
from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        print(dic)
        print(Counter(discount[i:i+10]))
        print('----------------------------')
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer

if __name__ == '__main__':
    result = solution(["banana", "apple", "rice", "pork", "pot"], 
                      [3, 2, 2, 2, 1], 
                      ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
                      )
    print(result)
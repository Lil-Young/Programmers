from itertools import product

def solution(word):
    answer = 0
    data = ["A", "E", "I", "O", "U"]
    l = []
    for i in range(1, 6):
        a = (list(product(data, repeat=i)))
        for d in a:
            l.append(''.join(list(d)))
    l.sort()
    answer = l.index(word) + 1
    return answer

if __name__ == '__main__':
    result = solution("AAAAE")
    print(result)
    result2 = solution("AAAE")
    print(result2)
    result3 = solution("I")
    print(result3)
    result4 = solution("EIO")
    print(result4)
def ascii(n, num):
    s = ""
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if num == 0:
        return ['0']
    while num > 0:
        s += number[num%n]
        num //= n
    s = list(s)
    s.reverse()
    return s

def solution(n, t, m, p):
    answer = ''
    ans = ''
    c = t*m
    for i in range(0, 1000000):
        if len(answer) > c:
            break
        s = ascii(n, i)
        for j in s:
            ans += j
    for i in range(p-1, c, m):
        answer += ans[i]

    return answer

if __name__ == '__main__':
    result = solution(2, 4,	2, 1) # "0111"
    print(result)
    # result2 = solution(16, 16, 2, 1) # "02468ACE11111111"
    # print(result2)
    # result3 = solution(16, 16, 2, 2) # "13579BDF01234567"
    # print(result3)
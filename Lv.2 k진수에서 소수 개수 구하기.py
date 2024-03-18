import math
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    result = ""
    while n > 0 :
        a = n%k
        result+=str(a)
        n = n//k
    result = list(result)
    result.reverse()
    result = ''.join(result)
    
    b = result.split('0')
    b = [int(x) for x in b if x != '']
    for i in b:
        if is_prime(i):
            answer+=1

    return answer

if __name__ == '__main__':
    result = solution(437674, 3)
    print(result)
    r = solution(110011, 10)
    print(r)
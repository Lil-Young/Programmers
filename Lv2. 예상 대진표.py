import math
def solution(n,a,b):
    answer = 0
    while True:
        if a == b:
            break
        a = a//2 + a%2
        b = b//2 + b%2
        answer+=1
    return answer

if __name__ == "__main__":
    result = solution(16, 4, 7)
    print(result)
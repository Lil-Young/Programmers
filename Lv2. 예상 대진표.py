def solution(n,a,b):
    answer = 0
    a, b = a-1, b-1
    while a != b:
        a = a//2
        b = b//2
        answer+=1
    return answer

if __name__ == "__main__":
    result = solution(16, 4, 7)
    print(result)
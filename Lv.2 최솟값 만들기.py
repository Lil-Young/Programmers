import math

def solution(A:list,B:list):
    answer = 0
    A, B = list(sorted(A)), list(reversed(sorted(B)))
    for i in zip (A, B):
        answer += math.prod(i)
    return answer

if __name__ == "__main__":
    result = solution([1, 4, 2], [5, 4, 4])
    print(result)
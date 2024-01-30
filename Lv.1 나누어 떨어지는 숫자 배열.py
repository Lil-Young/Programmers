def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    return answer if len(answer) != 0 else [-1]

if __name__ == "__main__":
    result = solution([3, 2, 6], 10)
    print(result)
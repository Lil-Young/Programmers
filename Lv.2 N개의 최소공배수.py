def solution(arr:list):
    answer = 0
    arr.sort()
    cnt = 0
    for i in range(2, 1000000):
        a = [x*i for x in arr]
        for j in a:
            for k in arr:
                if j%k == 0:
                    cnt += 1
                    if cnt == len(arr):
                        return j
            cnt = 0
    return answer

if __name__ == "__main__":
    result = solution([1, 2, 3])
    print(result)
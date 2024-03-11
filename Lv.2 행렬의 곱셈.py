def solution(arr1:list, arr2:list):
    a = len(arr2[0])
    b = len(arr1)
    answer = [[0] * a for _ in range(b)]

    for i, value1 in enumerate(arr1):
        print(i, value1)
        for k, value2 in enumerate(value1):
            for j in range(a):
                print(f"i, j, k: {i, j, k}")
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

if __name__ == '__main__':
    result = solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
    print(result)
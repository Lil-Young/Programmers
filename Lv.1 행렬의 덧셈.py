def solution(arr1, arr2):
    n_arr = [[0]*len(arr1[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            n_arr[i][j] = arr1[i][j] + arr2[i][j]
    return n_arr

if __name__ == "__main__":
    result = solution([[1], [2]], [[3], [4]])
    print(result)
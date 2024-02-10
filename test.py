N = int(input())
loc = list(map(str, input().split()))
arr = [[0] * N for i in range(N)]
arr[3][3] = 1
print(arr)
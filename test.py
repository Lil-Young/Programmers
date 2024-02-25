def binary_search(H, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    H_list = [x - mid for x in H if x - mid > 0]
    H_sum = sum(H_list)
    
    if H_sum == target:
        return mid
    elif H_sum > target:
        # 이진 탐색을 계속 수행
        result = binary_search(H, target, mid + 1, end)
        # 목표값에 도달하지 못하면 현재 mid 값을 반환
        return result if result is not None else mid
    else:
        return binary_search(H, target, start, mid - 1)

N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
result = binary_search(H, M, 0, max(H))
if result is None:
    print("원소가 존재하지 않습니다.")
else:
    print(result)

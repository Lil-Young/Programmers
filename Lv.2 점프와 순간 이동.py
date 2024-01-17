# case1: K 칸을 앞으로 점프 (k칸마다 건전지가 k만큼 닮)
# case2: 현재까지 온 거리 x 2에 해당하는 위치로 순간이동 (건전지 안듦)

def solution(n):
    ans = 0
    count = 1 # 만드려는 n
    jump_count = 0 # jump 카운트
    k_count = 1 # k 카운트
    while True:
        count *= 2
        if n < count:
            k_count += (n-(count//2))
            ans = k_count
            break
    return ans

result = solution(5000)
print(result)
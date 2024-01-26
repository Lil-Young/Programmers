# case1: K 칸을 앞으로 점프 (k칸마다 건전지가 k만큼 닮)
# case2: 현재까지 온 거리 x 2에 해당하는 위치로 순간이동 (건전지 안듦)
import math

def solution(n):
    count = 1
    while True:
        # n이 1이면 
        if n == 1:
            return count
        n = n/2 # 점프를 하는지 마는지 결정하기 위한 계산
        f_n = (n%1)*10 # f_n이 5면 1칸 앞으로 점프
        if f_n == 5:
            n = math.floor(n)
            count+=1
result = solution(1)
print(result)

T = int(input())
for _ in range(T):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    # array 초기화 및 입력 값 넣기
    array = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            array[i][j] = arr.pop(0)

    # 오른쪽 위, 오른쪽, 오른쪽 아래 좌표
    pos = [(0, 1), (1, 1), (-1, 1)]
    
    # 시작 인덱스 초기화
    start_idx = 0
    # 시작 값 초기화
    start_val = array[0][0]
    # 리스트의 첫번째 행에서 최댓값이 위치한 인덱스를 start_idx에 넣기
    for i in range(1, n):
        if array[i][0] > start_val:
            start_val = array[i][0]
            start_idx = (i, 0)
    # 금의 최대 크기를 첫번째 행의 최댓값으로 초기화
    total = start_val
    # 다음 행의 최댓값 구하기
    for _ in range(m-1):
        # 다음 행의 최댓값을 구하기 위한 변수 초기화
        temp = 0
        for i in pos:
            # 인덱스 에러 방지를 위한 예외처리
            try:
                # 현재 위치에서 오른쪽, 오른쪽 위, 오른쪽 아래의 값 중 최댓값 구하기
                if array[start_idx[0] + i[0]][start_idx[1] + i[1]] > temp:
                    idx1, idx2 = start_idx[0] + i[0], start_idx[1] + i[1]
                    temp = array[idx1][idx2]
            except:
                pass
        start_idx = (idx1, idx2)
        total += array[start_idx[0]][start_idx[1]]
    print(total)
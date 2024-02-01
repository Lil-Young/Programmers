def solution(board:list, moves:list):
    answer = 0 # 정답
    n_list = [] # 크레인으로 뽑은 인형 리스트

    # 크레인으로 인형 뽑기
    for i in range(len(moves)):
        for j in range(len(board)):
            if (board[j][moves[i]-1]) != 0:
                n_list.append((board[j][moves[i]-1]))
                board[j][moves[i]-1] = 0
                break

    # 뽑은 인형 리스트에서 같은 인형이면 해당 인형 삭제 및 answer += 2
    before, after = 0, 1
    while True:
        if after >= len(n_list): 
            break
        if n_list[before] == n_list[after]:
            del n_list[before:(after+1)]
            answer+=2
            before, after = 0, 1
        else:
            before += 1
            after += 1
    return answer

if __name__ == "__main__":
    result = solution([[1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [1, 0, 0, 0, 0], [3, 0, 0, 0, 0]], [1, 1, 1, 1])
    print(result)
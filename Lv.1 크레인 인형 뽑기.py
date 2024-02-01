def solution(board:list, moves:list):
    answer = 0
    n_list = []
    cpy_board = board
    for i in range(len(moves)):
        for j in range(len(board)):
            if (board[j][moves[i]-1]) != 0:
                n_list.append((board[j][moves[i]-1]))
                board[j][moves[i]-1] = 0
                break
    print(n_list)

    return answer

if __name__ == "__main__":
    result = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
    print(result)
def solution(friends: list, gifts: list):
    answer = [0] * len(friends)  # 각각 선물을 몇번 받는지에 관한 리스트
    index_list = []  # 비교를 하기 위한 index
    _list = [[0] * len(friends) for _ in range(len(friends))] # 준사람/받은사람 2차원 리스트

    # 비교하기 위한 인덱스 리스트 생성
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                index_list.extend([[i, j]])

    set_index_list = list(set([tuple(sorted(index_list)) for index_list in index_list]))  # 인덱스 중복제거

    # 준사람 선물 추가
    for i in gifts:
        spl_str = i.split()
        a = friends.index(spl_str[0])
        b = friends.index(spl_str[1])
        _list[a][b] += 1

    # 선물 지수
    futures_list = []
    for i, j in enumerate(_list):
        have_sum = 0
        for k in range(len(friends)):
            have_sum += _list[k][i]
        futures_list.append(sum(j) - have_sum)

    # 비교 및 받은 선물을 추가
    for i in set_index_list:
        if _list[i[0]][i[1]] == _list[i[1]][i[0]] or (_list[i[0]][i[1]] == 0 and _list[i[1]][i[0]] == 0):
            if futures_list[i[0]] > futures_list[i[1]]:
                answer[i[0]] += 1
            elif futures_list[i[0]] < futures_list[i[1]]:
                answer[i[1]] += 1
        else:
            if _list[i[0]][i[1]] > _list[i[1]][i[0]]:
                answer[i[0]] += 1
            else:
                answer[i[1]] += 1
    result = max(answer)
    return result

if __name__ == "__main__":
    result = solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"])
    print(result)

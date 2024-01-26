def solution(n, words):
    answer = []
    _list = []
    # num: 번호, order: 차례
    num, order = 0, 1
    count = 0
    for i in words:
        if num == n: 
            num = 0
            order += 1
        num += 1
        count += 1
        # 끝말잇기 안되는 경우, 이미 나왔던 단어인 경우, 한 글자인 단어인 경우
        if (count > 1 and _list[-1][-1] != i[0]) or (count > 1 and i in _list) or len(i) == 1:
            answer.extend([num, order])
            break
        elif len(words) == count:
            answer.extend([0, 0])
        _list.append(i)
    return answer

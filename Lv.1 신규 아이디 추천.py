def solution(new_id:str):
    answer = ''
    txt = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '-', '_', '.']

    # 대문자 -> 소문자, '-', '_', '.'을 제외한 특수문자 제거
    for i in new_id:
        if i.isalpha() and i.isupper():
            i = i.lower()
        if i not in txt:
            i = ''
        answer += i
    new_answer = []
    # 2번 이상 연속된 '.'을 하나의 '.'으로 치환
    for i in range(len(answer)):
        if answer[i:i+2] != "..":
            new_answer.append(answer[i])
    # '.'가 처음이나 끝에 위치하면 제거
    if new_answer[0] == '.':
        del new_answer[0]
    if len(new_answer) != 0: # 리스트에 아무것도 안들어있으면 new_answer[-1]에서 오류남
        if new_answer[-1] == '.':
            del new_answer[-1]
    # 빈 문자열이면 'a' 대입
    if len(new_answer) == 0:
        new_answer.append('a')
    # 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 삭제
        # 만약 제거 후 '.'가 끝에 위치한다면 끝에 위치한 '.' 문자 삭제
    if len(new_answer) >= 16:
        new_answer = new_answer[:15]
    # 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복
    elif len(new_answer) <= 2:
        for i in range(2):
            if len(new_answer) == 3:
                break
            new_answer.append(new_answer[-1])
    # '.'가 처음이나 끝에 위치하면 제거
    if new_answer[0] == '.':
        del new_answer[0]
    if len(new_answer) != 0: # 리스트에 아무것도 안들어있으면 new_answer[-1]에서 오류남
        if new_answer[-1] == '.':
            del new_answer[-1]
    answer = ''.join(new_answer)
    return answer

if __name__ == "__main__":
    result = solution("abcdefghijklmn.p")
    print(result)
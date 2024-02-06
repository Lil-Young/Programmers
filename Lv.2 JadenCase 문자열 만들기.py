def solution(s):
    answer = ''
    idx = 0 # 첫 단어는 0, 아니면 1
    for i in s:
        # i가 ' '이 아니고 단어중에 첫 문자면 대문자로 변환 후, answer에 추가
        if idx == 0 and i != ' ':
            answer += i.upper()
            idx += 1
        # i가 ' '이면 answer에 ' '추가
        elif i == ' ':
            answer += i
            idx = 0
        # i가 ' '이 아니고 단어중에 첫 문자가 아니면 소문자로 변환 후, answer에 추가
        else:
            answer += i.lower()        
    return answer

if __name__ == "__main__":
    result = solution("3people unFollowed me")
    print(result)
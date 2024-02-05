def solution(s):
    answer = 'a  b'
    print(answer, end = ' ')
    for i in s:
        print(i)
    return answer

if __name__ == "__main__":
    result = solution("a   b")
    print(result)
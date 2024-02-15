def solution(s):
    s = list(s)
    answer= -1
    temp = []
    for i in s:
        if len(temp) == 0:
            temp.append(i)
        else:
            if i == temp[-1]:
                temp.pop()
            else:
                temp.append(i)


    answer = 1 if len(temp) == 0 else 0

    return answer

if __name__ == "__main__":
    result = solution("baabaa")
    print(result)
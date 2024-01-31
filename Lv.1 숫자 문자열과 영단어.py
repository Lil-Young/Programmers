def solution(s):
    answer=""
    number_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    str_n = ""
    for i in s:
        if i.isdigit():
            answer+=i
        else:
            str_n += i
            if str_n in number_dict.keys():
                answer += number_dict.get(str_n)
                str_n = ""
    return int(answer)

if __name__ == "__main__":
    result = solution("one4seveneight")
    print(result)
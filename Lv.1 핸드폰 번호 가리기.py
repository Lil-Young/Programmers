def solution(phone_number):
    len_p = len(phone_number)-4
    result = "*"*len_p
    for i in range(len_p, len(phone_number)):
        result += phone_number[i]
    return result

if __name__ == "__main__":
    result = solution("027778888")
    print(result)
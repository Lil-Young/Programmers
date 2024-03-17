def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    print(hash_map)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                print(phone_number)
                print(temp)
                answer = False
    return answer


if __name__ == '__main__':
    result = solution(["119", "97674223", "1195524421"])
    print(result)
    # result1 = solution(["123","456","789"])
    # print(result1)
    # result2 = solution(["12","123","1235","567","88"])
    # print(result2)

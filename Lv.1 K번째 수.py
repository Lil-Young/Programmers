def solution(array:list, commands:list):
    answer = []
    cpy_array = array
    for i in commands:
        slice_list = cpy_array[i[0]-1:i[1]]
        slice_list.sort()
        answer.append(slice_list[i[2]-1])
    return answer

if __name__ == "__main__":
    result = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    print(result)
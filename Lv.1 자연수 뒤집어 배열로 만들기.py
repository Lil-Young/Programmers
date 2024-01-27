def solution(n):
    list_n = list(str(n))
    reverse_n_list = [int(list_n[x]) for x in range(len(list_n)-1, -1, -1)]
    return reverse_n_list

if __name__ == "__main__":
    result = solution(12345)
    print(result)
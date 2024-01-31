def solution(strings, n):
    answer = sorted(strings, key= lambda x:(x[n], x))
    return answer

if __name__ == "__main__":
    result = solution(["abce", "abcd", "cdx"], 2)
    print(result)
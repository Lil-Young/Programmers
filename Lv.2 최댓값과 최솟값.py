def solution(s):
    s_split = [int(x) for x in s.split()]
    answer = "{} {}".format(min(s_split), max(s_split))
    return answer

if __name__ == "__main__":
    result = solution("-1 -2 -3 -4")
    print(result)
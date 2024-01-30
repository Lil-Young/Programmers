def solution(s):
    s = sorted(s, reverse=True)
    return "".join(s)

if __name__ == "__main__":
    result = solution("gfedcbZ")
    print(result)
def solution(s):
    try:
        return bool((len(s) == 4 or len(s) == 6) and str(type(int(s))) == "<class 'int'>")
    except:
        return False

if __name__ == "__main__":
    result = solution("1123")
    print(result)
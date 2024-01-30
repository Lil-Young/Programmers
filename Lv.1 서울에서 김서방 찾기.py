def solution(seoul: list):
    answer = f"김서방은 {seoul.index("Kim")}에 있다"
    return answer

if __name__ == "__main__":
    result=  solution(["Jane","Kim"])
    print(result)
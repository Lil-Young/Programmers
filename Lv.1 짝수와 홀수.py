def solution(num: int):
    answer = "Even" if num%2 == 0 else "Odd"
    return answer

if __name__ == "__main__":
    result = solution(2)
    print(result)
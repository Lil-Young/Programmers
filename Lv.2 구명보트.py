def solution(people: list, limit: str):
    answer = 0
    asc_people = sorted(people)
    start, end = 0, len(people) - 1
    while start <= end:
        if asc_people[start] + asc_people[end] <= limit:
            answer+=1
            start+=1
            end-=1
        else:
            answer+=1
            end-=1
    return answer

if __name__ == "__main__":
    result = solution([80, 50, 50, 70], 100)
    print(result)

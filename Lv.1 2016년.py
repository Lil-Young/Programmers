import datetime
def solution(a, b):
    week_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return week_list[datetime.datetime(2016, a, b).weekday()]

if __name__ == "__main__":
    result = solution(5, 24)
    print(result)
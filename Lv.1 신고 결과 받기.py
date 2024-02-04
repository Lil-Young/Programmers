import collections

def solution(id_list, report, k:int):
    answer = []
    id_report_dict = {i:0 for i in id_list} # {사용자:신고당한 횟수}
    id_email_dict = {i:0 for i in id_list} # {사용자:메일 받는 횟수}
    report_list = [] # [{신고자:신고당한사람}]

    # report_list 리스트에 {신고자:신고당한사람} 추가
    for i in report:
        reporter, reported = i.split(" ")
        report_list.append({reporter:reported})

    # report_list 중복 제거
    report_list = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in report_list)))

    # report_list에서 딕셔너리 키, 값 반대로
    report_list_reverse = []
    for i in report_list:
        reverse_val = {v:k for k,v in i.items()}
        report_list_reverse.append(reverse_val)

    # {사용자:신고당한 횟수}에 횟수 추가
    for i in report_list:
        for j in i.values():
            id_report_dict[j] += 1

    # 처리 결과 메일
    stop = []
    for key, value in id_report_dict.items():
        if value >= k:
            stop.append(key)
    for i in report_list_reverse:
        for j in i.items():
            if j[0] in stop:
                id_email_dict[j[1]] += 1
    for i in id_email_dict.values():
        answer.append(i)
    return answer

if __name__ == "__main__":
    result = solution(["muzi", "frodo", "apeach", "neo"],
                      ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
                      2)
    result1 = solution(["con", "ryan"],
                        ["ryan con", "ryan con", "ryan con", "ryan con"],
                        3)
    print(result)
    print(result1)
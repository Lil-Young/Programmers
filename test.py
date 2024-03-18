def solution(id_list:list, report:list, k:int):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}
    print(reports)
    for r in set(report):
        reports[r.split()[1]] += 1
    print(reports)
    for r in set(report):
        print(r)
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

if __name__ == '__main__':
    result = solution(["muzi", "frodo", "apeach", "neo"],
                      ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
                      2)
    print(result)
    result1 = solution(["con", "ryan"],
                       ["ryan con", "ryan con", "ryan con", "ryan con"],
                       3)
    print(result1)

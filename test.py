def solution(id_list, report, k:int):
    answer = []
    print(id_list)
    print(set(report))
    print(k)
    return answer

if __name__ == '__main__':
    # result = solution(["muzi", "frodo", "apeach", "neo"],
    #                   ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    #                   2)
    # print(result)
    result1 = solution(["con", "ryan"],
                       ["ryan con", "ryan con", "ryan con", "ryan con"],
                       3)
    print(result1)
def solution(N:int, stages:list):
    answer = []
    failure_dict = {} # 각 스테이지 번호의 실패율을 담기 위한 딕셔너리
    set_stages = [x for x in range(1, N+1)] # 스테이지 번호를 리스트로 생성
    
    # {스테이지 번호:0} 으로 failure_dict에 넣기
    for i in set_stages:
        failure_dict[i] = 0

    # 각 스테이지를 클리어하지 못한 사용자가 몇명인지 failure_dict에 추가
    for j in stages:
        if j > len(set_stages):
            pass
        else:
            failure_dict[j] += 1

    # 실패율 딕셔너리 계산
    cnt = 0
    for k in set_stages:
        temp = failure_dict[k]
        # 0으로 나누는 경우 방지
        try:
            failure_dict[k] = failure_dict[k]/(len(stages)-cnt)
        except:
            failure_dict[k] = 0.0
        cnt += temp
    
    # 실패율 딕셔너리 역순으로 정렬한 리스트
    val_list = sorted(list(failure_dict.values()), reverse=True)

    # 실패율 리스트에 있는 값과 실패율 딕셔너리의 value를 비교해 같으면 answer에 추가 후 해당 딕셔너리 원소 삭제
    for i in val_list:
        for j in list(failure_dict.items()):
            if i==j[1]:
                answer.append(j[0])
                del failure_dict[j[0]]
    return answer

if __name__ == "__main__":
    result = solution(2, [3])
    print(result)
def solution(answers):
    answer = [0, 0, 0]
    give_up1 = [1, 2, 3, 4, 5]
    give_up2 = [2, 1, 2, 3, 2, 4, 2, 5]
    give_up3 = [3, 3, 1, 1 ,2, 2, 4, 4, 5, 5]
    for idx, i in enumerate(answers):
        idx1 = idx%len(give_up1)
        idx2 = idx%len(give_up2)
        idx3 = idx%len(give_up3)
        if i == give_up1[idx1]:
            answer[0] += 1
        if i == give_up2[idx2]:
            answer[1] += 1
        if i == give_up3[idx3]:
            answer[2] += 1
    answer_list = []
    max_num = max(answer)
    for idx, i in enumerate(answer):
        if max_num == i:
            answer_list.append(idx+1)
    
        
        
    return answer_list

if __name__ == "__main__":
    result = solution([1,3,2,4,2])
    print(result)
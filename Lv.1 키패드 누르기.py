def solution(numbers:list, hand:str):
    answer = '' # 정답
    left, right, middle = [1, 4, 7, "*"], [3, 6, 9, "#"], [2, 5, 8, 0]
    l_hand, r_hand = "*", "#" # 왼쪽 손가락, 오른쪽 손가락 초기화

    # for 문을 이용해 L 또는 R 넣는 작업
    for i in numbers:
        if i in left:
            answer += 'L'
            l_hand = i
        elif i in right:
            answer += 'R'
            r_hand = i
        else:
            ## 왼쪽, 오른쪽 손가락에서 해당 위치까지의 거리
            # 왼쪽, 오른쪽 손가락 둘다 키패드 왼쪽(1, 4, 7, '*'), 오른쪽(3, 6, 9, '#')에 있는 경우
            if l_hand in left and r_hand in right:
                dt1 = abs(left.index(l_hand) - middle.index(i)) + 1
                dt2 = abs(right.index(r_hand) - middle.index(i)) + 1
            # 왼쪽 손가락은 키패드의 중앙(2, 5, 8, 0), 오른쪽 손가락은 오른쪽에 있는 경우
            elif l_hand not in left and r_hand in right:
                dt1 = abs(middle.index(l_hand) - middle.index(i))
                dt2 = abs(right.index(r_hand) - middle.index(i)) + 1
            # 왼쪽 손가락은 키패드의 왼쪽, 오른쪽 손가락은 중앙에 있는 경우
            elif r_hand not in right and l_hand in left:
                dt1 = abs(left.index(l_hand) - middle.index(i)) + 1
                dt2 = abs(middle.index(r_hand) - middle.index(i))
            # 왼쪽, 오른쪽 손가락 둘다 키패드 중앙에 있는 경우
            else:
                dt1 = abs(middle.index(l_hand) - middle.index(i))
                dt2 = abs(middle.index(r_hand) - middle.index(i))
            # 거리가 가까운 손가락을 answr에 추가
            if dt1 < dt2:
                answer += "L"
                l_hand = i
            elif dt1 > dt2:
                answer += "R"
                r_hand = i
            else:
                if hand == "left":
                    answer += "L"
                    l_hand = i
                else:
                    answer += "R"
                    r_hand = i
    return answer

if __name__ == "__main__":
    result = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	, "left")
    print(result)
from bisect import bisect_left, bisect_right

def solution(citations:list):
    answer = 0
    citations.sort()

    for i in citations:
        left_index = bisect_left(citations, i)
        right_index = len(citations)
        num = right_index-left_index
        if i > num and answer < num:
            answer = num
        elif i <= num and answer < i:
            answer = i

    return answer

if __name__ == '__main__':
    result = solution([10, 8, 5, 4, 3])
    print(result)
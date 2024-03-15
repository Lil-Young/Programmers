import itertools
def solution(k, dungeons):
    answer = -1
    pmt = list(itertools.permutations(dungeons, len(dungeons)))
    cnt = 0
    sub_k = k
    while pmt:
        a = pmt.pop(0)
        for i in a:
            if k <= 0:
                break
            if i[0] <= k:
                k -= i[1]
                cnt += 1
        if cnt > answer:
            answer = cnt
        cnt = 0
        k = sub_k
        
    return answer

if __name__ == '__main__':
    result = solution(80, [[80,20],[50,40],[30,10]])
    print(result)
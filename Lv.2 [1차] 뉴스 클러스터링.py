# 문자만 남기기
# 모든 문자를 upper 또는 lower 하기
# 교집합/합집합 * 65536
from collections import Counter

def solution(str1:str, str2:str):
    answer = 0
    # str1, str2에 있는 문자열을 문자2개로 순서대로 나누고 문자로 이루어진 것을 대문자로 넣기
    s1, s2 = [str1[i-2:i].upper() for i in range(2, len(str1)+1) if str1[i-2:i].isalpha()], [str2[i-2:i].upper() for i in range(2, len(str2)+1) if str2[i-2:i].isalpha()]
    if len(s1) == 0 and len(s2) == 0:
        return 65536
    s1_dict, s2_dict = dict(Counter(s1)), dict(Counter(s2))

    # 합집합
    union_set = []
    for i in s2_dict.items():
        if i[0] not in s1_dict.keys():
            for _ in range(i[1]):
                union_set.append(i[0])
    for i in s1_dict.items():
        if i[0] in s2_dict.keys() and s2_dict[i[0]] > i[1]:
            for _ in range(s2_dict[i[0]]):
                union_set.append(i[0])
        else:
            for _ in range(i[1]):
                union_set.append(i[0])

    # 교집합
    intersection_set = []
    for i in s1_dict.items():
        l = 0
        if i[0] in s2_dict.keys():
            if s2_dict[i[0]] > i[1]:
                l = i[1]
            else:
                l = s2_dict[i[0]]
            for _ in range(l):
                intersection_set.append(i[0])
    answer = int((len(intersection_set) / len(union_set)) * 65536)
    return answer

if __name__ == '__main__':
    result = solution("aa1+aa2", "AAAA12")
    # result1 = solution("handshake", "shake hands")
    print(result)
    # print(result1)
    # r = solution("FRANCE", "french")
    # print(r)
    # a = solution("E=M*C^2", "e=m*c^2")
    # print(a)
    # b = solution("abc", "abbb")
    # print(b)

    # ab bc
    # ab bb bb
    # 합 = ab bb bb bc
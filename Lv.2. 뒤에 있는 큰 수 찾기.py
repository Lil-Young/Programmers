# numbers의 길이 = 1,000,000이므로 시간 복잡도는 O(NlogN) 또는 O(N)인 로직을 짜야된다.
def solution(numbers):
    stack = []  # 스택으로 활용할 리스트
    answer = [-1] * len(numbers)  # 결과를 저장할 리스트, 초기값은 -1로 설정

    for i in range(len(numbers)):
        # 스택이 비어있지 않고 현재 숫자가 스택의 가장 위에 있는 숫자보다 큰 경우
        while stack and numbers[stack[-1]] < numbers[i]:
            # 가장 가까이에 있는 뒷 큰수를 찾았으므로 결과 리스트에 해당 위치의 값을 갱신
            answer[stack.pop()] = numbers[i]
        # 현재 위치를 스택에 추가
        stack.append(i)
    return answer


if __name__ == '__main__':
    result2 = solution([9, 1, 5, 3, 6, 2])
    print(result2)

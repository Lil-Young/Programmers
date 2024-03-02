def solution(s):
    answer = 0
    s = list(s)
    for _ in range(len(s)):
        stack = []
        if s[0] in [')', '}', ']']:
            a = s.pop(0)
            s.append(a)    
            continue
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            try:
                stack[-1]
            except:
                continue
            if stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            elif stack[-1] == '[' and i == ']':
                stack.pop()
        if len(stack) == 0:
            answer+=1
        a = s.pop(0)
        s.append(a)

    return answer

if __name__ == '__main__':
    result = solution("}}}")
    print(result)
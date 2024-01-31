def solution(s:str, n):
    answer = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in s:
        if i == " ":
            answer += " "        
        elif i.isupper():
            idx = (alphabet.index(i.lower()) + n) % 26
            answer += alphabet[idx].upper()
        else:
            idx = (alphabet.index(i.lower()) + n) % 26
            answer += alphabet[idx]
    return answer

if __name__ == "__main__":
    result = solution("  a B z  ", 4)
    print(result)
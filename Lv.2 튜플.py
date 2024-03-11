def solution(s:str):
    s = s[1: len(s)-1]
    l = []
    t_l = []
    a = ''
    for i in s:
        if i.isdigit():
            a+=i
            continue
        if i==',' and a != '':
           t_l.append(int(a))
           a = ''

        if i == '{':
            t_l = []
        elif i == '}':
            if a != '':
                t_l.append(int(a))
                a = ''
            l.append(t_l)
    l.sort(key=len)
    
    n_l = []
    for i in l:
        for j in i:
            if j not in n_l:
                n_l.append(j)
    return n_l

if __name__ == '__main__':
    result = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
    print(result)
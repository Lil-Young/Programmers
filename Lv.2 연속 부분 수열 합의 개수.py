def solution(elements):
    cycle = elements + elements
    s = set()
    for i in range(len(elements)):
        for j in range(len(elements)):
            s.add(sum(cycle[i:i+j]))
    return len(s)

if __name__ == '__main__':
    result = solution([7,9,1,1,4])
    print(result)

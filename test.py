def solution(n,a,b):
    print(bin(((a-1))))
    print(bin(b-1))
    print(bin((a-1)^(b-1)))
    return ((a-1)^(b-1)).bit_length()

result = solution(8, 5, 7)
print(result)
def solution(n):
    bin_n = bin(n).count('1')
    new_n = 0
    while bin_n != new_n:
        n += 1
        new_n = bin(n).count('1')
    return n

if __name__ == "__main__":
    result = solution(15)
    print(result)
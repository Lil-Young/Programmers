def solution(n, m):
    if n > m:
        temp = n
        n = m
        m = temp
    copy_n, copy_m = n, m
    gcd_n, lcd_n = 0, 0
    r = 0
    # 최대공약수
    while n != 0 :
        r = m%n
        m = n
        n = r
    gcd_n = m
    # 최소공배수
    lcd_n = (copy_m*copy_n) // gcd_n
    return [gcd_n, lcd_n]
    
    
if __name__ == "__main__":
    result = solution(3, 12)
    print(result)
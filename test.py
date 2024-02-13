a = input()
x, y= ''.join(a)
_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
x = _dict[x]
x, y = int(x), int(y)
temp_x, temp_y = x, y
cnt = 0
nums = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
for n1, n2 in zip([num[0] for num in nums], [num[1] for num in nums]):
    x += n1
    y += n2
    if (x >= 1 and x <= 8) and (y >= 1 and y <= 8):
        cnt+=1
    x, y = temp_x, temp_y
print(cnt)


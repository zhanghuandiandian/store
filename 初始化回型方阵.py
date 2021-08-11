
num = int(input("输入那个不知道叫啥的："))
n = num * 2
m = [([0] * n) for i in range(n)]
for i in range(0, num):
    x = i+1
    for j in range(i, n-i):
        m[i][j] = x
        m[j][i] = x
        m[n-i-1][j] = x
        m[j][n-i-1] = x
for i in range(0, n):
    for j in range(0, n):
        print(str(m[i][j]) + "", end='')
    print('\n')



























# 输出质数方法一：
i = 2
while i < 100:
    j = 2
    f = True
    while j < i:
        if i % j == 0:
            f = False
        j += 1
    if f == True:
        print(i, ',', end='')
    i += 1
print('\n')

# 输出质数方法二：
f = True
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            f = False
            break
        else:
            f = True
    if f == True:
        print(i, ',', end='')
print('\n')
# 输出斐波那契数列迭代法：
a = [1, 1]
max = 20
for i in range(2, max):
    a.append(a[i - 1] + a[i - 2])

print(a)
print('\n')

# 输出斐波那契额数列递归法:
def fei(day):
    if day < 3:
        return 1
    else:
        return fei(day - 1) + fei(day - 2)


for i in range(1, 21):
    print(fei(i), end=' ')










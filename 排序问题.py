import time

# 冒泡排序
def bu(x):
    for j in range(len(x)-1):
        for i in range(0, len(x)-1-j):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
# 选择排序
def ss(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]

li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print('打印列表\n', li)
print('列表翻转\n', list(reversed(li)))
bu(li)
print('冒泡排序\n', li)
ss(li)
print('选择排序\n', li)

sir = 'sandilfuvbndjilc'
print('字符串统计\n', len(sir))


#读取日志文件
f = open(file="baidu_x_system.log", mode="r+", encoding="utf-8")
while True:
    m = f.readline()
    if m != "":
        print(f.readline())
        time.sleep(1)
    else:
        break
















# 使用+、-实现两个数的调换
A = 56
B = 78
print("A：", A, "B:", B)
A += B
B = A - B
A -= B
print("A：", A, "B:", B)

# 定义两个变量stu1和stu2，分别存储45和23，并用print打印两数之和
stu1 = 45
stu2 = 23
print("stu1:", stu1, "stu2:", stu2)

# 定义5个变量，并用print打印五个数的和，平均值
a = 1
b = 2
c = 3
d = 4
e = 5
f = a+b+c+d+e
print("五数之和：", f, "五数平均值：", f/5)

# 定义一个变量num1，并赋值45，然后将num1赋值给Num2，并打印出来
num1 = 45
num2 = num1
print("num2的值为：", num2)


# 一边删除a的数一边添加到a2里
a = [1, 2, 34, 56, 7, 45, 345, 345, 43, 34, 3, 56]
a2 = []
for i in range(len(a)):
    a2.append(a.pop())
print('a2', a2)
print('a', a)


i = 0
while i < len(a):
    a2.append(a.pop())
print('a2', a2)
print('a', a)
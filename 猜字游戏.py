'''
需求:
    1、猜字的数字是系统产生的，是不是自己定义的
    2、键盘上输入的     变量=input("提示语句")  print
    3、判断   if判断条件 elif判断条件 。。。。。。。。else
    4、循环    while 条件

    低级版本：
        while
        1、用户输入一个值
        2、判断值是多少
        if >随机数:猜对了
        else:猜错了
    高级版本：起始有5000块 猜错一次扣除500  如果猜了5次 没猜中 系统锁定   time.sleep
'''

import random
import time
num = random.randint(0, 101)
count = 0
a = 5000
while True:
    count = count + 1
    a = a - 500
    num_1 = input("输入个数：")
    num_1 = int(num_1)
    if count <= 5:
        if num_1 < num or num_1 > num:
            print("啥也没有")
        else:
            print("中奖了你")
            break
    else:
        time.sleep(2000)















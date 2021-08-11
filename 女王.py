'''
   姐就是女王 :
    随机选择人物： 1、普通没有技能  2、稀有英雄初始值为30。3、传奇英雄不会减少只会增加
    需求：
    初始值为：10
    随机生成三个数字
    进行选择一个数字（只有两秒的选择时间，超出后随机选择一个）
    选择的数字和初始值进行计算（随机加减）
    计算过后大于100则任务成功
    计算过后小于或等于0则任务失败

'''

from random import randint, choice, sample

list = ["普通英雄", "稀有英雄", "传奇英雄"]

while True:
    hero = choice(list)
    a = [randint(0, 101) for i in range(3)]
    b = choice('+-')
    if hero == '普通英雄':
        print('抽到了普通英雄')
        x = 10
        print(sample(a, 3))
        d = int(input('选个数：'))
        if b == '+':
            d_1 = x+d
            if d_1 >= 100:
                print('任务通关\n')
            elif d_1 < 100:
                print('任务失败\n')
        if b == '-':
            d_2 = x-d
            if d_2 >= 100:
                print('任务通关\n')
            elif d_2 < 100:
                print('任务失败\n')
    if hero == '稀有英雄':
        print('抽到了稀有英雄')
        x = 30
        print(sample(a, 3))
        d = int(input('选个数：'))
        if b == '+':
            d_1 = x + d
            if d_1 >= 100:
                print('任务通关\n')
            elif d_1 < 100:
                print('任务失败\n')
        if b == '-':
            d_2 = x - d
            if d_2 >= 100:
                print('任务通关\n')
            elif d_2 < 100:
                print('任务失败\n')
    if hero == '传奇英雄':
        print('抽到了传奇英雄')
        x = 10
        print(sample(a, 3))
        d = int(input('选个数：'))
        if x + d >= 100:
            print('任务通关\n')
        elif x + d < 100:
            print('任务失败\n')






























'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random

# 1.准备一个数据库 和 银行名称
bank = {}  # 空的数据库

'''
    {
        "张三":{
            account:s001,
            country:"中国"
        }，
        "李四":{

        }


    }

'''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


# 2.入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是狗已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if username in bank:
        return 2
    # 3.正常开户
    bank[username] = {
        "account": account,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "gate": gate,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型
    # 随机产生8为数字
    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, gate, money)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ------------------------
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))


# 存钱
'''
2.	存钱（传入值：用户的账号、存取的金额。返回值：布尔类型值）
a)	业务逻辑：
	先根据传入的账号信息查询用户库里是否有该用户。若没有则返回False
	若有，则将该用户的金额存进去。
'''
def put(num, password):
    for i in bank.keys():
        num = int(bank[i]["account"])
        print("账号为%d" % num)
        if password == int(bank[i]["password"]):
            print("密码为%d" % password)
            return True

        else:
            return False


def put_money():
    num = int(input("输入账号："))
    password = int(input("输入密码"))
    i = put(num, password)
    if i == True:
        for i in bank.keys():
            qian = int(input("输入存的钱："))
            int(bank[i]["money"])
            bank[i]["money"] = bank[i]["money"] + qian
            print("现在还剩%d" % bank[i]["money"])
    else:
        print("存钱失败了")


# 取钱
'''
3.	取钱（传入值：用户的账号，用户密码，取钱金额。返回值：整型值（0：正常，1：账号不存在，2：密码不对，3：钱不够））
a)	业务逻辑：
	先根据账号信息来查询该用户是否存在，若不存在，则返回代号1，
	若存在，则继续判断密码是否正确，若不正确，则返回代号2。
	若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱，若不满足，则返回代号3，
	若满足，则将该用户的金额减去。

'''
def qv_money():
    for i in bank.keys():
        add = input('输卡号：')
        password = input('输密码')
        add = int(bank[i]['account'])
        if password == bank[i]['password']:
            qv = int(input('取多少啊：'))
            if qv > bank[i]['money']:
                print('你钱不够！！')
            elif qv <= bank[i]['money']:
                bank[i]['money'] = bank[i]['money'] - qv
                print('取成功了！还有{}元'.format(bank[i]['money']))
            else:
                print('憋瞎写！')
        elif password != bank[i]['password']:
            print('密码不对！！！')
        else:
            print('没这用户憋瞎写！')


'''
4.	转账（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：账号不对，2密码不对，3钱不够）
a)	业务逻辑：
	先查询用户库是否存在转出和转入的账号，若不存在则返回代号,1，
	若账号都存在则继续判断转出账号的密码是否正确，若不正确，则返回2，
	若正确则继续判断要转出的金额是否足够，若不够则返回3，
	否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。

'''
def zhuan_money():
    add = input('你转的用户名：')
    zhuan = int(input('你转多少钱：'))
    for i in bank.keys():
        if i == add:
            bank[i]['money'] = bank[i]['money'] + zhuan
            print('转成功了啊')
        else:
            print('没这户！！！')

'''
1.	查询账户功能（传入值：账号，账号密码，返回值：空）
a)	业务逻辑：
	先根据账号判断用户库是否存在该用户，若不存在则打印提示信息：该用户不存在。
	否则继续判断密码是否正确。若不正确则打印相对应的错误信息。
	若账号和密码都正确，则将该用户的信息都打印出来，比如：当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.

'''
def cha_moeny():
    for i in bank.keys():
        add = input('输卡号：')
        password = input('输密码：')
        add = int(bank[i]['account'])
        if password == bank[i]['password']:
            info = '''
                ------------个人信息------------
                用户名:%s
                银行卡号：%s
                密码：%s
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
                余额：%s
                开户行名称：%s
                                '''
            print(info % (i,bank[i]["account"],bank[i]["password"],bank[i]["country"], bank[i]["province"], bank[i]["street"], bank[i]["gate"], bank[i]["money"], bank_name))
        elif password != bank[i]['password']:
            print('密码不对！！')
        else:
            print('没这户！！')



while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        put_money()
    elif chose == "3":
        qv_money()
    elif chose == "4":
        zhuan_money()
    elif chose == "5":
        cha_moeny()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")















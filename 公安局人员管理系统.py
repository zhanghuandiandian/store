import pymysql
con = pymysql.connect(host='localhost',user='root',password='root',database='mymy')
cursor = con.cursor()

dic_1 = {
    0:'个人荣誉',
    1:'国家级别荣誉奖章和国务院税务津贴',
    2:'无犯罪历史',
    3:'有过轻度犯罪历史',
    4:'严重犯罪历史',
    5:'杀人罪但是有期徒刑',
    6:'杀人罪并执行死刑'
}

dic_2 = {
    0:'没有教育历史(包括幼儿园)',
    2:'小学文化',
    3:'初中文化',
    4:'高中文化',
    5:'大学文化（硕士生）',
    6:'研究生',
    7:'教授',
}

dic_3 = {}
dic_4 = {}

class Address:
    __county = ''
    __province = ''
    __street = ''
    __door = ''
    def __init__(self,county,province,street,door):
        self.__county = county
        self.__province = province
        self.__street = street
        self.__door = door


    def setCounty(self,county):
        self.__county = county
    def getCounty(self):
        return self.__county

    def setProvince(self,province):
        self.__province = province
    def getProvince(self):
        return self.__province

    def setStreet(self,street):
        self.__street = street
    def getStreet(self):
        return self.__street

    def setDoor(self,door):
        self.__door = door
    def getDoor(self):
        return self.__door

    def show_1(self):
        print('国家',self.__county,'省份',self.__province,'街道',self.__street,'门牌号',self.__door)


class User(Address):
    __id = ''
    __name = ''
    __gender = ''
    __age = 0
    __password = 0
    __state = ''
    __add = ''
    __date = ''
    __immigrant = ''
    __reputation = ''
    __culture = ''
    __study = 0


    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setGender(self,gender):
        self.__gender = gender
    def __getGender(self):
        return  self.__gender

    def setAge(self,age):
        if age <= 0:
            print('非法了别乱写！！！')
        else:
            self.__age = int(age)
    def __getAge(self):
        return self.__age

    def setPassword(self,password):
        if password < 6 and password > 12:
            print('非法非法了啊！！！')
        else:
            self.__password = password
    def getPassword(self):
        return  self.__password

    def setState(self, state):
        if state != True or state != False:
            print('别瞎写，非法了！')
        else:
            self.__state = state
    def getState(self):
        return self.__state

    def setDate(self,date):
        self.__date = date
    def getDate(self):
        return self.__date

    def setImmigrant(self,immigrant):
        self.__immigrant = immigrant
    def getImmigrant(self):
        return self.__immigrant

    def setReputation(self,reputation):
        for key in dic_1:
            print(key, dic_1[key])
        self.__reputation = reputation
    def getReputation(self):
        return self.__reputation

    def setCulture(self,culture):
        for key in dic_2:
            print(key, dic_2[key])
        self.__culture = culture
    def getCulture(self):
        return self.__culture

    def setStudy(self,study):
        self.__study = study
    def getStudy(self):
        return self.__study

    def xuexi(self):
        print("")

    def learn(self, much):
        sql = 'select culture from user where name = "self.__id"'
        num_1 = cursor.execute(sql)
        if much >= num_1:
            sql = 'update user set study=study+1 where name = "self.__id"'
            cursor.execute(sql)
            return 1
        elif much < num_1:
            print('先学会上一级的！！！')
            return 0
        elif much > dic_2.keys():
            print('你超纲了啊你！！！')
            return 2

    def show(self):
        Address.show_1(self)
        print('身份证：',self.__id,
              '姓名:',self.__name,
              '性别：',self.__gender,
              '年龄：',self.__age,
              '密码：',self.__password,
              '状态：',self.__state,
              '居住地址：',Address.show_1,
              '注册日期：',self.__date,
              '申请移民日期：',self.__immigrant,
              '人员信誉程度：',self.__reputation,
              '文化程度：',self.__culture,
              '学习次数：',self.__study
              )

u = User()
a = input('输入身份证号')
print(u.setId(a))
b = input('输入名字')
print(u.setName(b))
c = input('输入性别')
print(u.setGender(c))
d = input('输入年龄')
print(u.setAge(d))
e = input('输入密码')
print(u.setPassword(e))
f = input('输入状态')
print(u.setState(f))
g = input('输入住国家')
print(u.setCounty(g))
h = input('输入省份')
print(u.setProvince(h))
i = input('输入街道')
print(u.setStreet(i))
j = input('输入门牌号')
print(u.setDoor(j))
k = input('输入注册日期')
print(u.setDate(k))
l = input('输入申请移民日期')
print(u.setImmigrant(l))
m = input('输入人员信誉度0-9：')
print(dic_2)
for i in range(6):
    if m == dic_2.keys():
        m_1 = dic_2.values()
        print(u.setReputation(m_1))
n = input('输入文化程度')
for i in range(7):
    if n == dic_2.keys():
        n_2 = dic_2.values()
        print(u.setCulture(n_2))
o = input('学习次数')
print(u.setStudy(o))

































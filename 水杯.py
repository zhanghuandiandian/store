'''
水杯：有高度，有容量，有颜色，能盛水

'''


class Pp:
    __high = 0
    __capacity = 0
    __colour = ''

    def sethigh(self, high):
        if high <= 0:
            print('你家水杯没高度！')
        else:
            self.__high = high

    def gethigh(self):
        return self.__high

    def setcapacity(self, capacity):
        if capacity < 0:
            print('容量能是负的吗！')
        else:
            self.__capacity = capacity

    def getcapacity(self):
        return self.__capacity

    def setcolour(self, colour):
        self.__colour = colour

    def getcolour(self):
        return self.__colour

    def hold(self, water):
        print('水杯里有', water)

    def show(self):
        print('水杯的高度是', self.__high, '厘米，容量是', self.__capacity, '毫升，颜色是', self.__colour)


p = Pp()
p.hold(str(input('水杯里有啥：')))
p.sethigh(int(input('输入高度：')))
p.setcapacity(int(input('输入容量：')))
p.setcolour((input('水杯啥颜色：')))
p.show()



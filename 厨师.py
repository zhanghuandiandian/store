import threading
import time
from threading import Thread

lock = threading.Lock()
basket = 0


# 厨师制作面包
class baker(Thread):
    lock = threading.Lock()

    def run(self) -> None:
        global basket
        t = 0
        while True:
            self.lock.acquire()
            if basket == 500:
                time.sleep(0.5)
                t += 0.5
                if t == 5:
                    print('顾客已将钱全部购买面包！')
                    break
            else:
                time.sleep(0.5)
                basket += 1
            self.lock.release()


# 顾客买面包
class customer(Thread):
    username = ''
    lock = threading.Lock()

    def run(self) -> None:
        money = 3000
        count = 0
        while True:
            self.lock.acquire()
            if money < 2:
                print(self.username, '顾客钱已花完，成功购买', count, '个面包。')
                break
            else:
                if basket < 1:
                    time.sleep(1)
                else:
                    count += 1
                    money -= 2
                    print('成功购买一个面包！')
            self.lock.release()


baker1 = baker()
baker2 = baker()
baker3 = baker()
customer1 = customer()
customer2 = customer()
customer3 = customer()
customer4 = customer()
customer5 = customer()
customer6 = customer()
customer1.username = '一号'
customer2.username = '二号'
customer3.username = '三号'
customer4.username = '四号'
customer5.username = '五号'
customer6.username = '六号'

baker1.start()
baker2.start()
baker3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
customer5.start()
customer6.start()




















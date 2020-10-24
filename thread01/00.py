import random
import threading
import time

num = 100

class Thread01:
    def print1(msg):
        time.sleep(random.randint(0, 10))
        print(f'{msg}')


# 自定义
class Thread02(threading.Thread):
    def __init__(self, msg):
        super().__init__()  # 重写run方法
        self.msg = msg

    def run(self):
        global num
        time.sleep(1)
        t.acquire()
        num=num-self.msg
        t.release()
        print(f'{self.msg},{num}')


if __name__ == '__main__':
    # t01 = Thread01()
    # for i in range(10):
    #     threading.Thread(target=t01.print1, args={i}).start()
    #线程锁
    # t=threading.Lock()
    # 信号量（BoundedSemaphore类)
    # 互斥锁同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去
    t=threading.BoundedSemaphore(2)
    for i in range(10):
        Thread02(i).start()
        # 设置线程守护 主线程执行完成后子线程自动关闭（不论是否执行完成）
        # t = Thread02(i)
        # t.setDaemon(True)  # 把子进程设置为守护线程，必须在start()之前设置
        # t.start()
        # #守护线程 主线程等待子线程执行  子线程不执行完成 主线程不不关闭
        # t.join()
        # print(f'end:{i}')

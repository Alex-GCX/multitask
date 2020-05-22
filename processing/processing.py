from multiprocessing import Process
import time
import os


def dancing():
    print('开始跳舞，进程号：%d' % os.getpid())
    for i in range(5):
        print('正在跳舞：。。。。%d' % i)
        time.sleep(0.5)
    print('结束跳舞')


def singing():
    print('开始唱歌，进程号：%d' % os.getpid())
    for i in range(5):
        print('正在唱歌：。。。。%d' % i)
        time.sleep(0.5)
    print('结束唱歌')


if __name__ == '__main__':
    # 创建对象
    p1 = Process(target=dancing)
    p2 = Process(target=singing)
    # 调用进程
    p1.start()
    p2.start()

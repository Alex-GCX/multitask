from multiprocessing import Process
import time
import os


def dancing(name, num, **kwargs):
    print('开始跳舞，进程号：%d, name=%s, num=%d, age=%d' % (os.getpid(), name, num, kwargs['age']))
    for i in range(num):
        print('%s正在跳舞：。。。。%d' % (name, i))
        time.sleep(0.5)
    print('结束跳舞')


def singing(name, num, **kwargs):
    print('开始唱歌，进程号：%d, name=%s, num=%d, age=%d' % (os.getpid(), name, num, kwargs['age']))
    for i in range(num):
        print('%s正在唱歌：。。。。%d' % (name, i))
        time.sleep(0.5)
    print('结束唱歌')


if __name__ == '__main__':
    # 创建对象
    p1 = Process(target=dancing, args=('xiaoming', 5), kwargs={'age': 10})
    p2 = Process(target=singing, args=('xiaohong', 10), kwargs={'age': 20})
    # 调用进程
    p1.start()
    p2.start()

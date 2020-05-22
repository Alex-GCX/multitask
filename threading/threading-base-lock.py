import time
import threading
g_num = 0


def dancing(num, mutex):
    global g_num
    for i in range(num):
        # 上锁
        mutex.acquire()
        # 计算
        g_num += num
        # 解锁
        mutex.release()

    print('dancing 线程结束,num值： %d' % g_num)


def singing(num, mutex):
    global g_num
    for i in range(num):
        # 上锁
        mutex.acquire()
        # 计算
        g_num += num
        # 解锁
        mutex.release()

    print('dancing 线程结束,num值： %d' % g_num)


def main():
    print('初始值：%d' % g_num)
    # 创建锁对象
    mutex = threading.Lock()
    # 创建子线程对象
    t1 = threading.Thread(target=dancing, args=(1000000, mutex, ))
    t2 = threading.Thread(target=singing, args=(1000000, mutex, ))
    # 子线程开始执行
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

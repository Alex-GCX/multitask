import time
import threading
g_num = 0


def dancing(num):
    global g_num
    for i in range(num):
        g_num += num
    print('dancing 线程结束,num值： %d' % g_num)


def singing(num):
    global g_num
    for i in range(num):
        g_num += num
    print('dancing 线程结束,num值： %d' % g_num)


def main():
    print('初始值：%d' % g_num)
    # 创建子线程对象
    t1 = threading.Thread(target=dancing, args=(1000000,))
    t2 = threading.Thread(target=singing, args=(1000000,))
    # 子线程开始执行
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

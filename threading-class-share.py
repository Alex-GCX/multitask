import threading
import time

g_num = 0


class DancingThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        global g_num
        for i in range(self.num):
            g_num += 1
        print('跳舞线程结束，g_num：%d' % g_num)


class SingingThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        global g_num
        for i in range(self.num):
            g_num += 1
        print('唱歌线程结束，g_num：%d' % g_num)


def main():
    # 创建Thread对象
    dancing = DancingThread(1000000)
    sing = SingingThread(1000000)
    # 调用run方法，开启线程
    print('初始g_num: %d' % g_num)
    dancing.start()
    sing.start()
    # 等待子线程运行完
    while len(threading.enumerate()) > 1:
        time.sleep(1)
    print('线程结束后g_num: %d' % g_num)


if __name__ == '__main__':
    main()

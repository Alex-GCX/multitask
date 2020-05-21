import threading
import time


class DancingThread(threading.Thread):
    def run(self):
        for i in range(1, 3):
            print('线程名：%s，正在跳舞：。。。%d' % (self.name, i))
            time.sleep(0.5)
        print('跳舞线程结束')


class SingingThread(threading.Thread):
    def run(self):
        for i in range(1, 5):
            print('线程名：%s，正在唱歌：。。。%d' % (self.name, i))
            time.sleep(0.5)
        print('唱歌线程结束')


def main():
    # 创建Thread对象
    dancing = DancingThread()
    sing = SingingThread()
    # 调用run方法，开启线程
    dancing.start()
    sing.start()


if __name__ == '__main__':
    main()

import time
import threading


def dancing():
    for i in range(1, 4):
        print('跳舞中%d' % i)
        time.sleep(0.5)
    print('dancing 线程结束')


def singing():
    for i in range(1, 5):
        print('唱歌中%d' % i)
        time.sleep(0.5)
    print('singing 线程结束')


def main():
    # 创建子线程对象
    t1 = threading.Thread(target=dancing)
    t2 = threading.Thread(target=singing)
    # 子线程开始执行
    t1.start()
    t2.start()
    # 查看正在运行的子线程数量
    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为：%d' % length)
        if length <= 1:
            break
        time.sleep(0.2)


if __name__ == '__main__':
    main()

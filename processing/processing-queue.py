from multiprocessing import Process, Queue
import time


def put(queue):
    for i in [11, 22, 33, 44, 55]:
        print('put: %d' % i)
        queue.put(i)
        time.sleep(0.5)


def read(queue):
    while not queue.empty():
        print('read: %d' % queue.get())
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建Queue对象
    queue = Queue()
    # 创建对象
    p1 = Process(target=put, args=(queue, ))
    p2 = Process(target=read, args=(queue, ))
    # 开始进程p1
    p1.start()
    # 等待p1运行完
    p1.join()
    print('queue是否满了：', queue.full(), ', 是否空了：', queue.empty())
    print('queue的大小为：%d' % queue.qsize())
    # 开始进程p2
    p2.start()
    # 等待p2运行完
    p2.join()
    print('queue是否满了：', queue.full(), ', 是否空了：', queue.empty())
    print('queue的大小为：%d' % queue.qsize())

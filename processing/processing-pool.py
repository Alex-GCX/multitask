from multiprocessing import Pool
import time
import os
import random


def worker(msg):
    start_time = time.time()
    print('----------%s开始执行，进程号%d' % (msg, os.getpid()))
    time.sleep(random.random())
    end_time = time.time()
    print('----------%s执行结束, 耗时%0.2f' % (msg, (end_time - start_time)))
    # 异常测试
    print('捕获下面的print异常前')
    try:
        print(1 + 'end')
    except Exception as e:
        print('捕获到异常')
    print('不捕获下面的print异常')
    print(1 + 'end')
    print('不捕获异常后')


def main():
    # 定义进程池,最大进程数为3
    pool = Pool(3)
    for i in range(1, 8):
        # 每次循环将会用空闲出来的子进程去调用目标
        pool.apply_async(worker, (i, ))
    print('------start------')
    # 关闭进程池，关闭后不再接收新的请求
    pool.close()
    # 等待pool中所有进程结束，必须放在close()后面
    pool.join()
    print('------end------')


if __name__ == '__main__':
    main()

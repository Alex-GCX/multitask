from multiprocessing import Pool
import time
import os


def worker(msg):
    start_time = time.time()
    print('%s开始执行，进程号%d' % (msg, os.getpid()))
    time.sleep(2)
    end_time = time.time()
    print('%s执行结束, 耗时%0.2f' % (end_time - start_time))


# def main():
#     # 定义进程池,最大进程数为3
#     pool = Pool(3)
#     for i in range(1, 10):
#         # 每次循环将会用空闲出来的子进程去调用目标
#         pool.apply_async(worker, (i, ))
#     pool.close()
#     pool.join()


# if __name__ == '__main__':
#     main()
# 定义进程池,最大进程数为3
pool = Pool(3)
for i in range(1, 10):
    # 每次循环将会用空闲出来的子进程去调用目标
    pool.apply_async(worker, (i, ))
pool.close()
pool.join()

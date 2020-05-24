import gevent
from gevent import monkey
import time

# 有耗时操作时，需要执行这句话
# 能将普通的耗时操作转换为gevent中的耗时操作，这样就不用手动把耗时操作全都替换成gevent中对应的耗时操作了
monkey.patch_all()


def work(name, num):
    for i in range(num):
        print('%s正在执行。。。。%d' % (name, i))
        time.sleep(0.2)


def main():
    dance = gevent.spawn(work, '小明', 5)
    sing = gevent.spawn(work, '小花', 6)
    gevent.joinall([dance, sing])


if __name__ == '__main__':
    main()

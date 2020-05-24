import time
from greenlet import greenlet


def dancing():
    for i in range(5):
        print('正在跳舞。。。。。%d' % i)
        sing.switch()
        time.sleep(0.1)


def singing():
    for i in range(5):
        print('正在唱歌。。。。。%d' % i)
        dance.switch()
        time.sleep(0.1)


# 创建全局greenlet对象
dance = greenlet(dancing)
sing = greenlet(singing)


def main():
    # 调用执行dance
    print('开始执行dance')
    dance.switch()


if __name__ == '__main__':
    main()

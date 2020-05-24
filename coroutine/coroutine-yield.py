import time


def dancing():
    for i in range(5):
        print('正在跳舞。。。。%d' % i)
        yield
        time.sleep(0.1)


def singing():
    for i in range(5):
        print('正在唱歌。。。。%d' % i)
        yield
        time.sleep(0.1)


def main():
    dance = dancing()
    sing = singing()
    for i in range(5):
        next(dance)
        next(sing)
        time.sleep(0.1)


if __name__ == '__main__':
    main()

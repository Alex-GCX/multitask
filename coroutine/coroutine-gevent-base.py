import gevent
import time


def dancing(n):
    for i in range(n):
        print('正在跳舞...%d' % i)
        # time.sleep(0.2)
        # 普通的耗时操作，如time.sleep、socket.recv()、socket.connect()等
        # 这些代码需要手动转换为gevent模块中对应的方法，才能被gevent认为是耗时操作
        # 当gevent遇到了认可的耗时操作后，就会自动切换通过gevent创建的对象
        # 若没有遇到耗时操作，则按顺序执行gevent对象
        gevent.sleep(0.5)


def singing(n):
    for i in range(n):
        print('正在唱歌...%d' % i)
        # time.sleep(0.2)
        gevent.sleep(0.5)


def main():
    print('--------main开始-------')
    # 创建对象，这时并没有执行方法里面的代码
    dance = gevent.spawn(dancing, 5)
    sing = gevent.spawn(singing, 6)
    # join()开始执行对象中对应的方法并等待方法执行完成
    # 在执行方法的过程中，遇到耗时操作，则自动会切换执行gevent对象中的其他方法。
    dance.join()
    sing.join()
    print('-------main结束--------')


if __name__ == '__main__':
    main()

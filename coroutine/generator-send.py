def fibonacci(num):
    a, b = 0, 1
    current = 0
    while current < num:
        # ret用来接收send()传入的参数，若是next()则ret为None
        ret = yield a
        print('ret:', ret)
        # 当ret不为None时，则将b设置为传入的新的起始值,如4，这样下一次遍历时，a = b = 4，就会从4往下开始返回了
        if ret:
            b = ret
        a, b = b, a + b
        current += 1


def main():
    f1 = fibonacci(10)
    print(next(f1))
    print(next(f1))
    # 除了next可以获取生成器下一个值外，还可以使用send()方法，区别就是send()支持传入一个参数
    # 这个传入的参数其中一个作用就是可以用来设置生成器下一次返回的起始值
    # f1.send(None)等价于next(f1)
    print(f1.send(None))
    # send(4)传入参数值4，在生成器中，使用传入参数处理想要的逻辑
    print(f1.send(4))
    print(f1.send(None))
    print(f1.send(None))


if __name__ == '__main__':
    main()

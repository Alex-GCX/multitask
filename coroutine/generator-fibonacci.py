def fibonacci(num):
    a, b = 0, 1
    current = 0
    while current < num:
        yield a
        a, b = b, a + b
        current += 1
    return '遍历完毕.....'


def main():
    f1 = fibonacci(10)
    f2 = fibonacci(10)
    f3 = fibonacci(5)
    # for循环比遍历生成器
    for i in f1:
        print(i)
    # list处理生成器
    print(list(f2))
    # while循环处理生成器
    while True:
        try:
            print(next(f3))
        except StopIteration as e:
            # 异常StopIteration的value属性即为生成器return的值
            print(e.value)
            break


if __name__ == '__main__':
    main()

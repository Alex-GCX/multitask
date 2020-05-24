import time


class Fibonacci(object):
    def __init__(self, num):
        self.a = 0
        self.b = 1
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.num:
            raise StopIteration
        temp = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current += 1
        return temp


def main():
    fibonacci_1 = Fibonacci(10)
    fibonacci_2 = Fibonacci(5)
    fibonacci_3 = Fibonacci(8)
    # for循环接收可迭代对象
    for i in fibonacci_1:
        print(i)
        time.sleep(0.2)
    # list接收可迭代对象
    lst = list(fibonacci_2)
    print(lst)
    # tuple接收可迭代对象
    tpl = tuple(fibonacci_3)
    print(tpl)


if __name__ == '__main__':
    main()

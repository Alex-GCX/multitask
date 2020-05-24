from collections.abc import Iterable, Iterator
import time


class MyList(object):
    """自定义迭代器"""

    def __init__(self):
        self.content = list()
        self.current = 0

    def add(self, value):
        self.content.append(value)

    def __iter__(self):
        return self

    def __next__(self):
        # 若越界则抛出StopIteration异常
        if self.current == len(self.content):
            raise StopIteration
        # 不越界则返回当前迭代的值，并自增下标current
        value = self.content[self.current]
        self.current += 1
        return value


def main():
    # 创建迭代器对象
    my_list = MyList()
    print('my_list是不是一个可迭代对象', isinstance(my_list, Iterable))
    print('my_list是不是一个迭代器', isinstance(my_list, Iterator))
    # 添加值
    my_list.add('小明')
    my_list.add('小红')
    my_list.add('小花')
    # 遍历my_list
    for value in my_list:
        print(value)
        time.sleep(0.5)


if __name__ == '__main__':
    main()

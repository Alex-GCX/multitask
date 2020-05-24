from collections.abc import Iterable
import time


class MyList(object):
    """自定义一个可迭代对象"""

    def __init__(self):
        self.content = list()

    def add(self, item):
        self.content.append(item)

    def __iter__(self):
        # 1.要使一个对象是可迭代对象，必须实现__iter__方法
        # 2.要使一个对象迭代时能每次都返回一个值，必须让__iter__返回一个迭代器对象
        # 创建迭代器对象
        myiterator = MyIterator(self)
        return myiterator


class MyIterator(object):
    """自定义一个迭代器，必须实现__iter__方法和__next__方法"""

    def __init__(self, mylist_obj):
        self.mylist = mylist_obj
        self.current = 0

    def __iter__(self):
        pass

    def __next__(self):
        """每次迭代时返回的值实际是通过__next__方法返回的"""
        # 1.定义一个下标current，每次调用时+1，用来实现每次调用__next__时，返回下一个值
        # 2.注意判断下标current自增时是否会越界，若越界则手动抛出StopIteration异常
        #   外层for循环迭代时，若遇到StopIteration异常，则会停止迭代
        if self.current == len(self.mylist.content):
            raise StopIteration
        value = self.mylist.content[self.current]
        self.current += 1
        return value


def main():
    my_list = MyList()
    my_list.add(11)
    my_list.add(22)
    my_list.add(33)
    print('my_list是不是可迭代对象：', isinstance(my_list, Iterable))
    my_list_iterator = iter(my_list)
    print('my_list返回的迭代器为：', my_list_iterator)
    print('my_list的下一个值为：', next(my_list_iterator))
    for i in my_list:
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    main()

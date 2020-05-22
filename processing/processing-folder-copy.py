import multiprocessing
import os


def file_copy(queue, folder_addr, new_addr, file_name):
    try:
        with open(folder_addr + '/' + file_name, 'rb') as f:
            content = f.read()
    except Exception as e:
        print('打开文件%s失败' % file_name)
        return
    try:
        with open(new_addr + '/' + file_name, 'wb') as f:
            f.write(content)
    except Exception as e:
        print('打开文件%s失败' % file_name)
    # 复制成功，将文件名放入队列中
    queue.put(file_name)


def main():
    while True:
        # 获取想要复制的文件夹
        folder_addr = input('请输入要复制的文件夹地址(exit退出)：\n')
        if folder_addr == 'exit':
            break
        # 判断该文件夹是否存在
        try:
            print(folder_addr)
            file_list = os.listdir(folder_addr)
        except Exception as e:
            print('输入的址不正确，正确格式如："D:/培训/26.python"')
            continue
        # 在该程序路径下创建文件夹
        new_addr = folder_addr + '[新]'
        try:
            os.mkdir(new_addr)
        except Exception as e:
            print('新文件夹创建失败，可能存在同名文件夹')
            continue
        # 创建队列
        queue = multiprocessing.Manager().Queue()
        # 创建进程池
        pool = multiprocessing.Pool(3)
        for file_name in file_list:
            pool.apply_async(file_copy, args=(queue, folder_addr, new_addr, file_name, ))
        print('----copy开始----')
        # 关闭进程池
        pool.close()
        # 等待进程池中程序运行完
        pool.join()
        print('----以下文件copy完成，新文件夹为%s----' % new_addr)
        # 打印copy成功的文件夹
        while not queue.empty():
            print(queue.get())


if __name__ == '__main__':
    main()

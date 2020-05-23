import multiprocessing
import os
import shutil
import time


def file_copy(success_queue, error_queue, folder_addr, new_addr, file_name):
    # 读取文件
    try:
        with open(folder_addr + '/' + file_name, 'rb') as f:
            content = f.read()
    except Exception as e:
        error_queue.put(file_name)
        return
    with open(new_addr + '/' + file_name, 'wb') as f:
        f.write(content)
    # 复制成功，将文件名放入队列中
    success_queue.put(file_name)


def main():
    while True:
        # 获取想要复制的文件夹
        folder_addr = input('请输入要复制的文件夹地址(exit退出),如："D:/培训/26.python：\n')
        if folder_addr == 'exit':
            break

        # 判断该文件夹是否存在
        try:
            file_list = os.listdir(folder_addr)
        except Exception as e:
            print('输入的址不正确，正确格式如："D:/培训/26.python"')
            continue
        # 在该程序路径下创建文件夹
        new_addr = folder_addr + '[新]'
        # 判断新文件夹是否已存在
        if os.path.exists(new_addr):
            flag = input('存在新的同名文件夹，是否覆盖？(Y/N)')
            if flag == 'N':
                continue
            # 删除原文件夹
            shutil.rmtree(new_addr)
        # 创建新文件夹
        try:
            os.mkdir(new_addr)
        except Exception as e:
            print('创建新文件夹%s失败' % new_addr)
            return

        # 创建队列
        success_queue = multiprocessing.Manager().Queue()
        error_queue = multiprocessing.Manager().Queue()
        # 创建进程池
        pool = multiprocessing.Pool(3)
        for file_name in file_list:
            pool.apply_async(file_copy, args=(success_queue, error_queue, folder_addr, new_addr, file_name, ))
        print('----copy开始----')
        # 关闭进程池
        pool.close()

        # 显示进度
        # 获取需下载总数
        total_length = len(file_list)
        while True:
            # 获取已完成个数
            success_length = success_queue.qsize()
            # 获取失败的个数
            error_length = error_queue.qsize()
            # 计算百分比
            print('\r已完成%0.2f%% [%d/%d]' % (success_length * 100 / total_length, success_length, total_length), end="")
            if success_length + error_length == total_length:
                break
            time.sleep(0.01)
            # 等待进程池中程序运行完
        pool.join()
        print('\n----以下%d个文件copy失败----' % error_length)
        while not error_queue.empty():
            print(error_queue.get())


if __name__ == '__main__':
    main()

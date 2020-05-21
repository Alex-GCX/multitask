import socket
import threading


def send_msg(udp_client, server_addr):
    while True:
        # 获取想要发送的数据
        send_data = input('请输入想要发送的数据(exit退出)：\n')
        # 发送数据
        if send_data == 'exit':
            udp_client.close()
            break
        udp_client.sendto(send_data.encode('utf-8'), server_addr)


def recv_msg(udp_client):
    while True:
        # 接收数据
        recv_data = udp_client.recvfrom(1024)
        # 打印接收数据
        print('接收数据为：%s' % recv_data[0].decode('utf-8'))


def main():
    print('--------------客户端------------------')
    # 创建套接字
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置客户端地址
    client_addr = ('localhost', 8909)
    udp_client.bind(client_addr)
    # 设置服务器地址
    server_addr = ('localhost', 8910)
    # 创建发送线程对象
    send_thread = threading.Thread(target=send_msg, args=(udp_client, server_addr))
    # 创建接收线程对象
    recv_thread = threading.Thread(target=recv_msg, args=(udp_client,))
    # 启动线程
    send_thread.start()
    recv_thread.start()


if __name__ == '__main__':
    main()

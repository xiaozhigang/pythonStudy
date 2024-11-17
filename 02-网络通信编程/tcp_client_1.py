import socket

if __name__ == '__main__':
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(('127.0.0.1', 8888))
    send_content = "hello server"
    send_data = send_content.encode('utf-8')
    tcp_client_socket.send(send_data)
    recv_data = tcp_client_socket.recv(1024)
    recv_data = recv_data.decode('utf-8')
    print('recv_data:', recv_data)
    tcp_client_socket.close()
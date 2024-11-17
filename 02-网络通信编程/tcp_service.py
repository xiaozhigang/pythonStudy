import socket
import threading


def handle_client_request(ip_port, client_socket):
    print("client ip and port: ", ip_port)
    while True:
        recv_data = client_socket.recv(1024)
        if recv_data:
            print("recv data length is: ", len(recv_data))
            recv_content = recv_data.decode("utf-8")
            print("recv data content is: ", recv_content)
            send_content = "问题处理中"
            send_data = send_content.encode("utf-8")
            client_socket.send(send_data)
        else:
            print("client is close")
            break
    client_socket.close()


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 8888))
    tcp_server_socket.listen(128)
    while True:
        new_client, ip_port = tcp_server_socket.accept()
        thread = threading.Thread(target=handle_client_request, args=(ip_port, new_client))
        thread.setDaemon(True)
        thread.start()

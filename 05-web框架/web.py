import socket
import threading
from http.client import responses

import framework

class HttpWebServer:

    def __init__(self, port):
      tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
      tcp_server_socket.bind(('', port))
      tcp_server_socket.listen(128)
      self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(new_socket):
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            new_socket.close()
            return

        recv_content = recv_data.decode("utf-8")
        print(recv_content)

        request_list = recv_content.split(' ', maxsplit=2)
        request_path = request_list[1]
        print(request_path)

        if request_path == '/':
            response_content = '/index.html'

        if request_path.endswith('.html'):
            """动态请求"""
            env = {"request_path": request_path}
            status, headers, response_content = framework.handle_request(env)
            print(status, headers, response_content)

            response_line = "HTTP/1.1 %s\r\n" % status
            response_header = ""

            for header in headers:
                response_header += "%s: %s\r\n" % header

            response_data = (response_line + response_header + "\r\n" + response_content).encode("utf-8")

            new_socket.send(response_data)
            new_socket.close()
        else:
            """静态请求"""
            try:
                with open("static" + request_path, "rb") as file:
                    file_data = file.read()
            except Exception as ret:
                response_line = "404 not found".encode("utf-8")
                response_header = "Server: PWS/1.1".encode("utf-8")
                with open("static/error.html", "rb") as file:
                    file_data = file.read()
                response_content = file_data
                response = (response_line + response_header + "\r\n".encode("utf-8") + response_content)
                new_socket.send(response)
            else:
                response_line = "HTTP/1.1 200 OK".encode("utf-8")
                response_header = "Server: PWS/1.1".encode("utf-8")
                response_content = file_data
                response = (response_line + response_header + "\r\n".encode("utf-8") + response_content)

                new_socket.send(response)

            finally:
                new_socket.close()

    def start(self):
        while True:
            new_socket, client_addr = self.tcp_server_socket.accept()
            thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            thread.setDaemon(True)
            thread.start()


def main():
    http_server = HttpWebServer(8000)
    http_server.start()

if __name__ == '__main__':
    main()



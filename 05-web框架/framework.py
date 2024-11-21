import time



def index():
    status = "200 OK"
    response_header = [("Server", "PWS/1.1")]
    data = time.ctime()

    return status, response_header, data

def not_find():
    status = "404 Not Found"
    response_header = [("Server", "PWS/1.1")]
    data = "Not Found"

    return status, response_header, data

def handle_request(env):
    request_path = env["request_path"]
    print("动态资源请求的地址：", request_path)
    if request_path == "/index":
        return index()
    else:
        return not_find()
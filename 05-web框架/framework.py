import json
import time

import pymysql
from OpenSSL.rand import status

route_list = []

def route(path):
    def decorator(func):
        route_list.append((path, func))
        def inner():
            return func()
        return inner
    return decorator

@route("/index.html")  # => @decorator => index = decorator(index)
def index():
    status = "200 OK"
    response_header = [("Server", "PWS/1.1")]
    with open("template/index.html", "r", encoding="utf-8") as file:
        file_data = file.read()

    conn = pymysql.connect(host="47.92.119.44",
                           port=3306,
                           user="root",
                           password="xiao@17719442576",
                           database="study",
                           charset="utf8")
    cursor = conn.cursor()
    sql = "select * from info;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()

    data = ""
    for row in result:
        data += """
        <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
        </tr>
        """ % row
    response_body = file_data.replace("{%content%}",data)
    return status, response_header, response_body


@route("/center_data.html")
def center_data():
    conn = pymysql.connect(host="47.92.119.44",
                           port=3306,
                           user="root",
                           password="xiao@17719442576",
                           database="study",
                           charset="utf8")
    cursor = conn.cursor()
    sql ='''
            select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info 
            from info i 
            inner join focus f on i.id = f.info_id;
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    center_data_list = [{
        "code": row[0],
        "short": row[1],
        "chg": row[2],
        "turnover": row[3],
        "price": str(row[4]),
        "highs": str(row[5]),
        "note_info": row[6]
    }for row in result]

    json_str = json.dumps(center_data_list, ensure_ascii=False)
    print(json_str)
    print(type(json_str))
    cursor.close()
    conn.close()
    status = "200 OK"
    response_header = [("Server", "PWS/1.1"),
                       ("Content-Type", "application/json;charset=utf-8")]
    return status, response_header, json_str

@route("/center.html")
def center():
    status = "200 OK"
    response_header = [("Server", "PWS/1.1")]
    with open("template/center.html", "r", encoding="utf-8") as file:
        file_data = file.read()
    response_body = file_data.replace("{%content%}", "")
    return status, response_header, response_body


def not_find():
    status = "404 Not Found"
    response_header = [("Server", "PWS/1.1")]
    data = "Not Found"

    return status, response_header, data

def handle_request(env):
    request_path = env["request_path"]
    print("动态资源请求的地址：", request_path)

    for path, func in route_list:
        if request_path == path:
            return func()
    return not_find()

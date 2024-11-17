import pymysql

if __name__ == '__main__':
    connect = pymysql.connect(host='47.92.119.44',
                              user='root',
                              password='xiao@17719442576',
                              database='dw_spider',
                              charset='utf8')
    cursor = connect.cursor()
    sql = 'select * from goods limit 10'
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connect.close()

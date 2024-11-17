import pymysql

if __name__ == '__main__':
    connect = pymysql.connect(host='47.92.119.44',
                              user='root',
                              password='xiao@17719442576',
                              database='dw_spider',
                              charset='utf8')

    cursor = connect.cursor()
    sql = 'update site set id = 1 where id = 173'

    try:
        cursor.execute(sql)
        connect.commit()
    except:
        connect.rollback()
    finally:
        cursor.close()
        connect.close()

import pymysql
if __name__ == '__main__':
    #创建链接对象  database：操作的数据库
    conn = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         port=3306,
                         database='test',
                         charset="UTF8")
    #获取游标，目的就是要执行sql语句
    cursor=conn.cursor()

    #准备sql语句
    sql="select * from one;"
    #执行sql语句
    cursor.execute(sql)
    #获取查询的结果,返回的数据类型是一个元组
    # row=cursor.fetchone()#获取一条数据
    # print(row)
    # 获取多条数据，返回的是一个元组，每条数据都是一个元组
    result=cursor.fetchall()
    for row in result:
        print(row)
    #关闭游标
    cursor.close()
    #关闭链接
    conn.close()






import pymysql

conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306,
                       database='test',  # 要操作的数据库名字
                       charset="UTF8")

cursor = conn.cursor()  # 获取游标， 目的是要执行sql语句
# sql="select * from one where name ='%s';"% "'黄蓉'or 1=1 or ''"
can = "'黄蓉'or 1=1 or ''"
sql = "select * from one where name =%s;" % can
print(sql)  # ==>>"select * from one where name ='黄蓉'or 1=1 or '';"
cursor.execute(sql)  # 执行sql语句
result = cursor.fetchall()  # 获取多条数据，返回的是一个元组，每条数据都是一个元组
for row in result:
    print(row)
# 关闭游标
cursor.close()
# 关闭链接
conn.close()

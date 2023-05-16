import pymysql

conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306,
                       database='test',  # 要操作的数据库名字
                       charset="UTF8")

cursor = conn.cursor()  # 获取游标， 目的是要执行sql语句

# can = ("'黄蓉'or 1=1 or ''")
can=("黄蓉")
# sql = "select * from one where name =%s;" % can
sql = "select * from one where name =%s;"  #防止sql注入就不在此处传参，在执行的时候传参
"""此时%s是sql语句的参数，不做字符串里的占位符
使用时在执行时传元组类型的参数"""

cursor.execute(sql,can)  # 执行sql语句
result = cursor.fetchall()  # 获取多条数据，返回的是一个元组，每条数据都是一个元组
for row in result:
    print(row)
# 关闭游标
cursor.close()
# 关闭链接
conn.close()

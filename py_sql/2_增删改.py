#创建链接对象  database：操作的数据库
import pymysql
"""
增删改时 与查询的不同是 要把修改的操作提交到数据库（commit）
"""

conn = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         port=3306,
                         database='test',
                         charset="UTF8")
#获取游标，目的就是要执行sql语句
cursor=conn.cursor()

#准备sql语句
#对数据表完成添加、删除修改操作，x需要吧修改的数据提交到数据库
sql="insert into one(note) values ('python57');" # 增

sql2="UPDATE one SET note = 'python63' where id = 002;"  # 改
sql3="DELETE FROM one WHERE id=003 ;" # 删

for i in ("2", "003", "004"):
    p='python'+i
    sq="UPDATE one SET note ='ssa' where id = "+i+" ;"  # 改
    try:
        #执行sql语句
        cursor.execute(sq)
        conn.commit() # 提交修改的数据库
        print("OK")
    except Exception as e:
        #对修改的数据进行撤销（数据的回滚（回到没有修改数据之前的状态））
        conn.rollback()
        print("ERROR")


# try:
#     #执行sql语句
#     cursor.execute(sql2)
#     conn.commit() # 提交修改的数据库
#     print("OK")
# except Exception as e:
#     #对修改的数据进行撤销（数据的回滚（回到没有修改数据之前的状态））
#     conn.rollback()
# 关闭游标
cursor.close()
# 关闭链接
conn.close()



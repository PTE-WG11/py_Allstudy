import pymysql
import uuid

'''
    数据库操作模块
'''


def create_uid():
    return str(uuid.uuid1())


# def Myargs(carId, owner, sex, phone, uid=''):
#     if uid:
#         tuple = (carId, owner, sex, phone, uid)


def get_conn():
    # 根据自己的实际修改
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='root', passwd='123456', db='graduation')
    return conn


def select_(sql, args=''):
    conn = get_conn()  # 建立连接
    cur = conn.cursor()  # 获取游标，目的就是要执行sql语句
    if args:
        num = cur.execute(sql, args)  # 执行sql语句 并且传入 数据
    else:
        num = cur.execute(sql)  # 执行sql语句 并且传入 数据
    print('查询到', num, '条数据')
    result = cur.fetchall()  # 获取多条数据，返回的是一个元组，每条数据都是一个元组
    # print(rsl)
    conn.commit()
    cur.close()
    conn.close()
    return result
def insert_(sql, args):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    print('成功插入', result, '条数据')
    conn.commit()
    cur.close()
    conn.close()
def delete_(sql, args):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    print('成功删除', result, '条数据')
    conn.commit()
    cur.close()
    conn.close()
def select():
    # if carID:
    #     args = ('carID', carID)
    #     sql = 'select * from cars WHERE carID = %s;'
    # elif Owner:
    #     args = ('Owner', Owner)
    #     sql = 'select * from cars WHERE Owner = %s;'
    # else:
    #     args = ('', '')
    #     sql = "select * from cars;"
    # print('args', args[1])
    sql = 'select * from scenery;'
    return select_(sql)
def insert(NO, ardress='', shengfen='', city='', placeName='',level='', x='', y='', note='', EAddress=''):
    args = (create_uid(), NO, ardress, shengfen, city, placeName,level, x, y, note, EAddress)
    # sql = 'INSERT INTO pathdesign_scenery VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    sql = 'INSERT INTO scenery VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    insert_(sql, args)
def delete(args):
    sql = 'DELETE FROM scenery WHERE id = %s;'
    # args = (1,)
    delete_(sql, args)
# 删除之前记录
def delete_all():
    sql = 'DELETE FROM scenery;'
    conn = get_conn()
    db = conn.cursor()
    db.execute(sql)
    conn.commit()
    print("系统初始化完成...")


if __name__ == '__main__':
    # args1 = (2,1,2,13,0,0)
    # insert(args1)
    # args = (2,)
    # delete(args)
    # delete_all()
    insert(NO='880880', ardress='山东济南', shengfen='', city='济南', name='', jingdu='', weidu='', note='', EAddress='')
    lis = select()
    print(lis)

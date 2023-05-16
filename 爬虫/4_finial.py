from 自动化.mysql_op import insert
from 自动化.read_excel import readip

lis_1 = readip("D://map-location.xlsx")  # [address, x, y]
lis_3=[]
with open('info_noName++_jingdian.txt', 'r', encoding='utf-8') as f:
    lis_2 = eval(f.read())  # [NO, placeName, label, address, Eaddress +x +y]

    # print(lis_2)
    # print(type(lis_2))
    # print(len(lis_1))
    # print(len(lis_2))

for i in range(len(lis_1)):
    print(lis_1[i][0], lis_2[i][3])
    if lis_1[i][0] == lis_2[i][3]:
        print('------')
        # lis_2 [NO, placeName, label, address, Eaddress]
        # lis_1 [address, x, y]
        # lis_3.append()
        lis_2[i].append(lis_1[i][1])
        lis_2[i].append(lis_1[i][2])

for i in lis_2:
    print(i)
for i in range(len(lis_2)):

    insert(NO=lis_2[i][0], ardress=lis_2[i][3],
           shengfen='山东', city='济南', placeName=lis_2[i][1],
           level=lis_2[i][2], x=lis_2[i][5], y=lis_2[i][6],
           note='', EAddress=lis_2[i][4])

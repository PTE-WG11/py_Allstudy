'''
本文件实现了两个文件信息的合并，保存至info_noName++_jingdian.txt
以字符串列表保存，使用时候，去除引号及可使用
合并后信息为 [NO, placeName, label, address, Eaddress]
'''

lis1 = []  # [placeName, Eaddress, label]
lis2 = []  # [NO, address, placeName]
lisAdd = []  # [NO, placeName, label, address, Eaddress]
with open(r'info_jingdian.txt', 'r', encoding='utf-8') as one:
    with open(r'info_+no_jingdian.txt', 'r', encoding='utf-8') as two:
        num = 1
        for info in one.readlines():
            c = info.rstrip().split(' ')
            lis1.append(c)
        for info2 in two.readlines():
            c = info2.rstrip().split(' ')
            lis2.append(c)
        for i in range(len(lis1)):
            if lis1[i][0] == lis2[i][2]:
                # [NO, placeName, label, address, Eaddress]
                mid = [lis2[i][0], lis1[i][0], lis1[i][2], lis2[i][1], lis1[i][1]]
                lisAdd.append(mid)
                print(num,mid)
                num+=1
        with open('info_noName++_jingdian.txt','w', encoding='utf-8') as  three:
            three.write(str(lisAdd))
        # print(lis1)
        # print(lis2)
        # print(len(lis1))
        # print(len(lis2))

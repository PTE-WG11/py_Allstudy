import time

from 自动化.suim import auto_NO

'''
本模块核心，操作自动化获取邮编放入文件info_+no_jingdian.txt
'''
with open(r'info_name_jingdian.txt', 'r', encoding='utf-8') as one:
    with open(r'info_+no_jingdian.txt', 'a+', encoding='utf-8') as two:
        num = 1
        for placeName in one.readlines():
            placeName = placeName.strip('\n')
            # print(placeName)
            NO, address = auto_NO(placeName=placeName)  # 核心，操作自动化获取邮编
            time.sleep(5)
            if NO != '0':
                # NO, address = ('212311','山东济南')
                NO.strip()
                address.strip()
                print(num, address, NO, placeName)
                two.write(NO + ' ' + address + ' ' + placeName + '\n')

            # else:
            #     two.write('NULL' + ' ' + address + '\n')
            num += 1

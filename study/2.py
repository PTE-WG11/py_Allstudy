zz = ''
if zz == '1':
    print("true")
elif zz == '2':
    pass
else:
    print('c')

for i in range(2, 10, 3):
    print(i)

"""f = open('')

f.close()
with open() as f:
    f.write()"""


# while(True):
#     pass
#     continue
#     break

def sda(can1, can2='21', can3='212', *lis, **ar):
    return None


def sda1(*lis):
    pass
def sda2(**ar):
    # ar={"can3":'sas', 'can1':'das'}
    pass

sda(can3='sas', can1='das')
sda1('dad', 'da', 'dad', 'da', 'dad', 'da', 'dad', 'da')
sda2(can3='sas', can1='das')

# import time
# import random


class Cat:
    def __init__(self):
        self.i = 0
    def das(self,da):
        self.i=''
        da='dd'
    def __str__(self):
        return 'dsa'
c=Cat()
print(c)

try:
    pass
except :
    pass
# 文件打开
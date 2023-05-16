with open(r'info_+no_jingdian.txt', 'r', encoding='utf-8') as two:
    for line in two.readlines():
        c=line.split()
        print(c[1])
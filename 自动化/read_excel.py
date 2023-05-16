import xlrd


def readip(f):
    '''
    读取xsl文件前三列，以数组返回
    '''
    # 校验文件是否存在，及文件格式
    data = xlrd.open_workbook(f)
    print(type(data))
    # table = data.sheet_by_name('Sheet1')
    table = data.sheet_by_index(0)  # 从0开始的sheet index，sheet1 计为0，类似数组索引
    print(type(table))
    nrows = table.nrows  # 获取行数
    # nclon = table.nclon

    result = []
    for i in range(1, nrows):
        rows = table.row_values(i)  # 是一个数组来按行获取
        # print(len(rows))

        # result.append(rows[0] + ':' + str(rows[1]).split('.')[0])
        # print(rows)
        result.append([rows[0], str(rows[1]), str(rows[2]) ])
    print(result)
    return result


if __name__ == "__main__":
    readip("D://map-location.xlsx")
# path = r'xlsx文件的路径'
# sheetName = '目标sheet的名称'
# data = xlrd.open_workbook(path)
# table = data.sheet_by_name(sheetName)

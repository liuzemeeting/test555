import xlrd
import xlwt
from xlwt import *


def data_write(file_path, datas):  # datas是列表
    print(datas)
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    # 将数据写入第 i 行，第 j 列
    for j_index, j in enumerate(datas):
        print(j_index, j)
        for index, i in enumerate(j):
            # print(index, i)
            sheet1.write(j_index, index, i)

    f.save(file_path)  # 保存文件


if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [5, 6, 7, 8]
    data_write("4.xls", list1)
    data_write("3.xls", list2)


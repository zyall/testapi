import xlrd
from conf import *
class ExcelUtil():
    '''
    返回格式为[{'rowNum': 2, '姓名': 1.0, '年龄': 18.0}, {'rowNum': 3, '姓名': 1.0, '年龄': 20.0}]

    '''
    def __init__(self, excelPath, sheetIndex=0):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_index(sheetIndex)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i+2
                values = self.table.row_values(j)
                # print(values)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

if __name__ == "__main__":
    filepath = xlsPath+'/test.xlsx'
    data = ExcelUtil(filepath, sheetIndex=0).dict_data()
    print(data)
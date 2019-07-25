import os
import csv
from conf import xlsPath



def get_parent_path(current_path):
    """获取路径的上一级"""
    return os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

def get_data_csv(filename):
    numbers = []
    with open(filename,'r',encoding='utf-8') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            numbers.append(row)
    return numbers


filename = xlsPath + '/test.csv'
print(get_data_csv(filename))
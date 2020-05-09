from  matplotlib import pyplot as plt
from pandas import read_excel
import pandas as pd
'''测试一个excel表格，并分析相关的数据'''

def read_excel1():
    df = pd.read_excel('2017蚌埠学院研究生名单.xls')  # 这个会直接默认读取到这个Excel的第一个表单
    data = df.head()  # 默认读取前5行的数据
    print("获取到所有的值:\n{0}".format(data))  # 格式化输出

if __name__ == '__main__':
    read_excel1()
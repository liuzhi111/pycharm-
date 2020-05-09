import sys
import os
from os import path


from  matplotlib import pyplot as plt
import pandas as pd
import numpy as  np
'''测试一个excel表格，并分析相关的数据'''


def read_excel1():
    df = pd.read_excel('2017蚌埠学院研究生名单.xls',index_col=0,usecols=[1,5],dtype={'姓名': str, '考上学校及专业': str})  # 这个会直接默认读取到这个Excel的第一个表单
    # 读取到表格数据  判断是不是985 211院校
    list1 = ['清华大学','北京大学','中国人民大学','中国科学技术大学','南京大学','东南大学','上海交通大学','复旦大学',
             '华东师范大学','']
    list2=['合肥工业大学','安徽大学','南昌大学','东华大学','河海大学','']
    print("获取到所有的值:\n{0}".format(df))  # 格式化输出


def mat():

    fix,ax = plt.subplots()
    ax.plot([1,2,3,4],[1,4,2,3])

if __name__ == '__main__':
    read_excel1()

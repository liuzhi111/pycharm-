import pandas as pds
import os
import os.path

import re

lt = re.match('www', 'www.taobao.com').span()
print(lt)

ls = []


def getAppointFile(path, ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path, tmp)
            if True == os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind('.') + 1:].upper() == 'PY':
                ls.append(pathTmp)
    except PermissionError:
        pass


def main():
    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path) == True:
            break

    getAppointFile(path, ls)
    print(ls)
    print(len(ls))

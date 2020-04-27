from time import time


def find_max(data):
    """Return the maximum element from a nonempty Python List"""
    biggest = data[0]
    for var in data:
        if var > biggest:
            biggest = var
    return biggest

import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total),path)
    return total


# 二分查找的实例


if __name__ == '__main__':
    path = 'H:/Project/PythonProject/2020.3.13/'
    print(disk_usage(path))
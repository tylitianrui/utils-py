# -*- coding: UTF-8 -*-
# author: tyltr
import time


#  获取时间戳
def timestamp():
    return time.time()


#  获取时间戳  秒级
def timestamp_sec():
    return int(time.time())


if __name__ == '__main__':
    print(timestamp())

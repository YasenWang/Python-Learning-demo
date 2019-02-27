#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '
#==========================
import time as t
def SimpleTextProgressBar():
    scale = 10
    print("======执行开始======")
    for i in range(scale + 1):
        a = '*' * i
        b = '·' * (scale - i)
        c = (i/scale)*100
        print("{:^3.0f}%[{}->{}]".format(c, a, b))
        t.sleep(0.1)
    print("======执行结束======")

def TextProgressBarPro():
    for i in range(101):
        print("\r{:3}%".format(i), end="")
        t.sleep(0.1)

def FullTextProgressBar():
    scale = 50
    print("执行开始".center(scale//2,"-"))
    start = t.perf_counter()
    for i in range(scale + 1):
        a = '*' * i
        b = '·' * (scale - i)
        c = (i / scale) * 100
        dur = t.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
        t.sleep(0.1)
    print("\n"+"执行结束".center(scale//2,"-"))
#==========================
if __name__ == '__main__':
    #pass
    #SimpleTextProgressBar()
    #TextProgressBarPro()
    FullTextProgressBar()
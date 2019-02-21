#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '

count = 0
while count <= 100:
    if count == 50:
        pass
    if count >= 60 and count <= 80:
        print("Loop ^2", count**2)
    else:
        if count %2 == 0:#偶数
            print("Loop ", count)
    count += 1
print("----End----\n")
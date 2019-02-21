#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '


# Tempstr = input("Please input the temperature with signal:\n")
# if Tempstr[-1] in ['F', 'f']:
#     C = (eval(Tempstr[0:-1]) - 32)/1.8
#     print("Convert Temperature is {:.2f}C\n".format(C))
# elif Tempstr[-1] in ['C', 'c']:
#     F = 1.8*eval(Tempstr[0:-1]) + 32
#     print("Convert Temperature is {:.2f}F\n".format(F))
# else:
#     print("Input Type Error!\n")

Tempstr = input()
if Tempstr[0] in ['F', 'f']:
    C = (eval(Tempstr[1:]) - 32)/1.8
    print("C{:.2f}\n".format(C))
elif Tempstr[0] in ['C', 'c']:
    F = 1.8*eval(Tempstr[1:]) + 32
    print("F{:.2f}\n".format(F))
else:
    print("输入格式错误\n")
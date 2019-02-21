#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '

MoneyStr = input()

if MoneyStr[0:3] == "RMB":
    USD = eval(MoneyStr[3:])/6.78
    print("USD{:.2f}\n".format(USD))
else:
    RMB = eval(MoneyStr[3:])*6.78
    print("RMB{:.2f}\n".format(RMB))
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '
def DayUp(dayfactor):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + dayfactor)
    return dayup

DayFactor = 0.01
while DayUp(DayFactor) < 37.78:
    DayFactor += 0.001
print("工作日的努力参数是:{:.3f}.".format(DayFactor))
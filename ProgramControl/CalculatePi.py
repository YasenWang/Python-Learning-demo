#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '
#==========================
from random import random
from time import perf_counter

def CalculatePiV1():
    pi = 0
    N = 100
    for k in range(N):
        pi += 1/pow(16, k)*\
              (4/(8*k + 1) - 2/(8*k + 4) -
               1/(8*k + 5) - 1/(8*k + 6))
    print("圆周率值是: {}".format(pi))

def MonteCarloCalculate():
    DARTS = 2000**2
    hits = 0.0
    start = perf_counter()
    for i in range(1, DARTS+1):
        x, y = random(), random()
        dist = pow(x**2 + y**2, 0.5)
        if dist <= 1.0:
            hits += 1
    pi = 4 * (hits/DARTS)
    print("圆周率的值是: {}".format(pi))
    print("运行时间是: {:.5f}s".format(perf_counter()-start))

#==========================
if __name__ == '__main__':
    # CalculatePiV1()
    MonteCarloCalculate()
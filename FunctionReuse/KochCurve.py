#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '
#==========================
import turtle

def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)

def KochSnow(size = 400, level = 3):
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    for i in range(3):
        koch(size, level)
        turtle.right(120)
    turtle.hideturtle()
    turtle.done()

def main():
    KochSnow()

#==========================
if __name__ == '__main__':
    main()
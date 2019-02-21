#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '

name:       str = input("Name: ")
age:        int = int(input("age: "))
job:        str = input("Job:")
hometown:   str = input("Hometown:")

info: str = '''
-----------------------------
Name       = %s
Age        = %d
Job        = %s
Hometown   = %s
-----------------------------
''' % (name, age, job, hometown)

print(info)


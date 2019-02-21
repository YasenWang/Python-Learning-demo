#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '

age: int = 26
user_guess = int(input("Input your guess age:\n"))

# print(type(user_guess))

if user_guess == age:
    print("Congratulations!\n")
elif user_guess < age:
    print("Try bigger\n")
else:
    print("Try smaller\n")
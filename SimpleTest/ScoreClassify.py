#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '
score = int(input("Score:\n"))

if score > 100:
    print("The max of the score is 100!\n")
elif score >=90 and score <= 100:
    print("Level: A\n")
elif score >= 80 and score <90:
    print("Level: B")
elif score >= 60 and score <80:
    print("Level: C")
elif score >= 40 and score <60:
    print("Level: D")
elif score >= 0 and score < 40:
    print("Level: E")
else:
    print("Error!")
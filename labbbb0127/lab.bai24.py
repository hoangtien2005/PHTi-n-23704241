# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:36:11 2024

@author: Tiến 
"""

a = int(input("Nhập vào số giờ:"))
b = int(input("Nhập  vào số phút:"))
c = int(input("Nhập vào số giây:"))
if 0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 59:
    print("giờ, phút, giây hợp lệ")
else:
    print("giờ, phút,giây không hợp lệ")
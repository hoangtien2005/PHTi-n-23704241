# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:28:18 2024

@author: Tiến
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
max_value = a
if b > max_value:
    max_value = b
if c > max_value:
    max_value = c
print("Giá trị lớn nhất là:",max_value)
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:02:10 2024

@author: Tiến
"""

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
d = int(input("Nhập số nguyên thứ tư: "))
min_value = a 
if b < min_value:
    min_value = b
if c < min_value:
    min_value = c
if d < min_value:
    min_value = d
print("Số nhỏ nhất là:",min_value)
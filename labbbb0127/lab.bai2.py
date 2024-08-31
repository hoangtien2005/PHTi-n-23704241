# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:13:18 2024

@author: Tiến 
"""

a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b if b != 0 else 'Khong the chia cho 0'
print("tong la = ", tong)
print("hieu la = ", hieu)
print("tich la = ", tich)
print("thuong la = ", round(thuong, 3))

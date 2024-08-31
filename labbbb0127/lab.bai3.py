# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:17:10 2024

@author: Tiến
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
chialaydu = a % b if b != 0 else 'khong the chia cho 0'
chialaynguyen = a // b if b != 0 else 'Khong the chia cho 0'
print("chia lay du la = ", str(chialaydu))
print("chia lay nguyen la = ", str(chialaynguyen))

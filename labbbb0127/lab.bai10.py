# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:59:30 2024

@author: Tiến 
"""

a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))
c = int(input("Nhap so c:"))
d = int(input("Nhap so d:"))
T = a + b + c + d 
if 0<T<10:
    print("So nut cua xe la:", T)
elif T>=10:
    sonut = T//10 + T%10
    print("So nut cua xe la:", sonut)
else:
    print("Khong xac dinh")

    
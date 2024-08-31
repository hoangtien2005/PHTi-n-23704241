# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:31:37 2024

@author: Tiến
"""

a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
c = int(input("Nhập số c:"))
if a>b and b>c:
    if a>c:
        print(f"{c} {b} {a}")
    else:
        print(f"{b} {c} {a}")
elif b>a and b>c:
    if a>c:
        print(f"{c} {a} {b}")
    else:
        print(f"{a} {c} {b}")
else: 
    if a>b:
        print(f"{b} {a} {c}")
    else:
        print(f"{a} {b} {c}")
        
        
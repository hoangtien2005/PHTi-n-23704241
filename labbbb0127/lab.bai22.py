# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:36:39 2024

@author: Tiến 
"""

print("Giải phương trình bậc nhất ax + b = 0")
a = float(input("a="))
b = float(input("b="))
if a!=0:
    x = -b/a
    print("Phương trình có nghiệm duy nhất:",x)
elif a == 0 and b!=0:
    print("Phương trình vô nghiệm")
elif a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Không xác định")

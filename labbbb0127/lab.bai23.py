# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:34:52 2024

@author: Tiến
"""

print("Giải phương trình bậc hai: a(x**2)+bx+c:")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a == 0:
    print("Phương trình không phải phương trình bậc hai")
elif a!=0:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + delta**(1/2))/2*a
        x2 = (-b - delta**(1/2))/2*a
        print("Phương trình có hai nghiệm")
        print("x1=",x1)
        print("x2=",x2)
    elif delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        print("Phương trình có nghiệm kép")
        print("x=",x)
else:
    print("Không xác định")
    
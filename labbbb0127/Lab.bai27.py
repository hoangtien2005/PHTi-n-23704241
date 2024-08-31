# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:59:40 2024

@author: Tiến
"""

a = float(input("Nhập chiều dài của hình chữ nhật:"))
b = float(input("Nhập chiều rộng của hình chữ nhật:"))
e = float(input("Nhập cạnh của hình vuông:"))
r = float(input("Nhập bán kính của hình tròn:"))
Cn = (a+b)*2
Sn = a*b
Cv = e*4
Sv = e*e
Ct = r*2*3.14
St = r*r*3.14
print("C vuông=",Cv, "\nS vuông=",Sv,"\nC tròn= ",Ct,"\nS tròn =",St,"\nC chữ nhật=",Cn,"\nS chữ nhật= ",Sn)


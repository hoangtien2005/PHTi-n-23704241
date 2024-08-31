# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:45:42 2024

@author: PC
"""

a = float(input("Nhap can nag cua ban a(kg):"))
b = float(input("Nhap chieu cao cua ban b(m):"))
BMI = a/(b*b)
if BMI<16:
    print("So do kiem tra suc khoe cua ban la:",BMI)
elif 16<=BMI<17:
    print("So do kiem tra suc khoe cua ban la:",BMI)
elif 17<=BMI<18.5:
    print("So do kiem tra suc khoe cua ban la:",BMI)
elif 18.5<=BMI<25:
    print("So do kiem tra suc khoe cua ban la:",BMI)
elif 25<=BMI<30:
    print("So do kiem tra suc khoe cua ban la:",BMI)
elif 30<=BMI<35:
    print("So do kiem tra suc khoe cua ban la:",BMI)
elif 35<=BMI<40:
    print("So do kiem tra suc khoe cua ban la:",BMI)
elif BMI>40:
    print("So do kiem tra suc khoe cua ban la:",BMI)
else:
    print("Khong xac dinh")
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:38:48 2024

@author: Tiến
"""

so = int(input("Nhập số:"))
chu = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
s_c={0:"không",
     1:"một",
     2:"hai",
     3:"ba",
     4:"bốn",
     5:"năm",
     6:"sáu",
     7:"bảy",
     8:"tám",
     9:"chín"}
if so in s_c:
    print(s_c[so])
else:
    print("Không đọc được")
    

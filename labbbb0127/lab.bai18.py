# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:27:00 2024

@author: Tiến 
"""

a = input("Nhập vào giờ phút giây thứ nhất theo dạng hh/mm/ss: ")
b = input("Nhập vào giờ phút giây thứ hai theo dạng hh/mm/ss: ")
hh, mm, ss= map(int,a.split("/"))
HH, MM, SS= map(int,b.split("/"))
if 0 <= hh <=23 and 0 <= mm <= 59 and 0 <= ss <= 59 and 0 <= HH <=23 and 0 <= MM <= 59 and 0 <= SS <=59:
   T = (hh + HH)*3600+(mm + MM)*60+ss+SS
   gio1 = T // 3600
   phut1 = gio1 // 60
   giay1 = T % 60
   print("tổng là:",gio1,"/",phut1,"/",giay1)
   H = (hh - HH)*3600+(mm - MM)*60+ss-SS
   gio2 = H // 3600
   phut2 = gio2 // 60
   giay2 = H % 60
   print("Hiệu của giờ thứ nhất với giờ thứ hai là:",gio2,"/",phut2,"/",giay2)
else:
    print("Không hợp lệ")

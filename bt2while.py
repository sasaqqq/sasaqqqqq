# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:33:12 2024

@author: Student
"""

a = float(input("Nhập số thực a="))
while -90.0 >= a or 89.9 <= a:
    a= float(input("Nhập lại số thực a="))
print("Giá trị đã nhập:", a)
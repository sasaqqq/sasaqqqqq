# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:19:54 2024

@author: Student
"""

a = int(input("Nhập số a="))
while -100>= a or 100 <= a:
    a = int(input("Nhập lại a="))
print("Giá trị đã nhập", a)

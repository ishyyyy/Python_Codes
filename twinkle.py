# -*- coding: utf-8 -*-
"""
Created on Tue May 18 20:45:29 2021

@author: ishur
"""

f=open('test.txt')
t=f.read()
if 'twinkle' in t:
    print("twinkle is present in t")
else:
    print("twinkle is not present in t")
    f.close()
    
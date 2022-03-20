# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:33:39 2018

@author: User
"""

from math import pi

G = 6.67e-11
M = 5.97e24
R = 6371e3
t1 = float(input("Enter the greater desired period in hours: "))
t2 = float(input("Enter the lesser desired period in hours: "))
T1,T2 = t1*60*60,t2*60*60

h1,h2 = ((G*M*T1**2)/(4*pi**2))**(1/3) - R, ((G*M*T2**2)/(4*pi**2))**(1/3) - R

print("The greater altitude is ", h1, " meters.")
print("The lesser altitude is ", h2, " meters.")
print("The deviation is ", h1-h2, " meters.")
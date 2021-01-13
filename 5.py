# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:17:12 2019

@author: prajw
"""
def fours(d):
    fourn = 0
    for i in d[1:]:
        try:
            n = int(i[3])
        except:
            n=0
        fourn += n
    print("The number of Fours hit by "+name+" in his overall career are",fourn)

nam = input("Enter the name of the player : ").split()  #for sample enter SachinTendulkar
name =""
for i in nam:
    name += i
from csv import reader
opened_file = open(name+".csv")
read_file = reader(opened_file)
data = list(read_file)
fours(data)
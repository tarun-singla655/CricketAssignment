# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:30:34 2019

@author: prajw
"""
def fours(data):
    fours = 0    
    for i in data[1:]:
        try:
            n=int(i[3])
        except:
            n = 0
        if (fours < n):
            fours = n
    print("The maximum number of Fours hit by "+name+" in an inning (among all innings he has batted) is",fours)
            


try:
    nam = input("Enter the name of the player : ").split()  #for sample enter SachinTendulkar
    name =""
    for i in nam:
        name += i
    from csv import reader
    opened_file = open(name+".csv")
    read_file = reader(opened_file)
    data = list(read_file)  
    fours(data)
except:
    print("Invalid Name")
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:31:54 2019

@author: prajw
"""

def fif(d):
    count = 0
    for i in d[1:]:
        runs=0
        if(i[0][-1]=='*'):
            runs=int(i[0][:-1])
        else:
            try:
                runs=int(i[0])
            except:
                runs=0
        if runs>50:
            count+=1
            
        
    print("PlayerName scores a fifty on an average after "+str(count/(len(d)-1))+" matches.")

try:
    nam = input("Enter the name of the player : ").split()  #for sample enter SachinTendulkar
    name =""
    for i in nam:
        name += i
    from csv import reader
    opened_file = open(name+".csv")
    read_file = reader(opened_file)
    data = list(read_file)  
    fif(data)
except:
    print("Invalid Name")
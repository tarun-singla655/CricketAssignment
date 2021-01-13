# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:43:09 2019

@author: prajw
"""
import numpy as np
import matplotlib.pyplot as plt

def fours(d):
    dicf={}
    for row in data[1:]:
        year = row[11][-2:]
        if(year not in dicf):
            dicf[year]=0
        n=0
        try:
            n=int(row[3])
        except:
            n=0
        dicf[year]+=n
        
    for x in dicf:
        print("Year : "+x+" has number of fours = "+str(dicf[x]))
    l = [i for i in dicf]
    hf = [dicf[i] for i in dicf]
    X = np.arange(len(l))
    w = 0.35
    fig,ax = plt.subplots()
    rct1 = ax.bar(X-w/2,hf,w,label="Highest")
    ax.set_ylabel('Number of Fours')
    ax.set_title('Fours by Years')
    ax.set_xticklabels(l)
    ax.legend()
    plt.show()
    

nam = input("Enter the name of the player : ").split()  #for sample enter SachinTendulkar
name =""
for i in nam:
    name += i
from csv import reader
opened_file = open(name+".csv")
read_file = reader(opened_file)
data = list(read_file)
fours(data)
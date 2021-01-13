# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:37:44 2019

@author: prajw
"""
import matplotlib.pyplot as plt
def run(d):
    runy={}
    for r in data[1:]:
        year = r[11][-2:]
        if(year not in runy):
            runy[year]=0
        runs=0
        if(r[0][-1]=='*'):
            runs=int(r[0][:-1])
        else:
            try:
                runs=int(r[0])
            except:
                runs=0
        runy[year]+=runs
    for i in runy:
        print("Year: "+str(i)+" Runs Scored "+ str(runy[i]))
    count = 0
    cfruny={}
    for i in runy:
        count+=runy[i]
        cfruny[i] = count
    new_dic = {}
    for x in cfruny:
        if(int(i)>=00 and int(x)<=19):
            new_dic[2000+int(x)]=cfruny[x]
        else:
             new_dic[1900+int(x)]=cfruny[x]
    X = [x for x in new_dic]
    plt.plot(X,[new_dic[x] for x in new_dic])
    plt.show()

nam = input("Enter the name of the player : ").split()  #for sample enter SachinTendulkar
name =""
for i in nam:
    name += i
from csv import reader
opened_file = open(name+".csv")
read_file = reader(opened_file)
data = list(read_file)
run(data)
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:14:03 2019

@author: prajw
"""

def scores(data):
    max1={}
    for r in data[1:]:
        year = r[11][-2:]
        if(year not in max1):
            max1[year]=0
        runs=0
        if(r[0][-1]=='*'):
            runs=int(r[0][:-1])
        else:
            try:
                runs=int(r[0])
            except:
                runs=0
        if(max1[year]<runs):
            max1[year]=runs
    max2={}
    for r in data[1:]:
        year = r[11][-2:]
        if(year not in max2):
            max2[year]=0
        runs=0
        if(r[0][-1]=='*'):
            runs=int(r[0][:-1])
        else:
            try:
                runs=int(r[0])
            except:
                runs=0
        if(max1[year]!=runs):
            if(max2[year]<runs):
                max2[year]=runs
                
    for x in max1:
        print("Year : "+x+" has highest runs = "+str(max1[x]))
        print("Year : "+x+" has max2ond highest runs = "+str(max2[x]))
        
    import numpy as np
    import matplotlib.pyplot as plt
    labels=[x for x in max1]
    firstHighest=[max1[x] for x in max1]
    max2ondHighest=[max2[x] for x in max2]
    
    X=np.arange(len(labels))
    fig,ax = plt.subplots()
    width=0.35
    rects1=ax.bar(X-width/2, firstHighest, width,label='Highest')
    rects2=ax.bar(X+width/2, max2ondHighest, width, label='second Hiighest')
    ax.set_ylabel('Scores')
    ax.set_title('Run by Years')
    ax.set_xticks(X)
    ax.set_xticklabels(labels)
    ax.legend()
    plt.show()

try:
    nam = input("Enter the name of the player : ").split()  #for sample enter SachinTendulkar
    name =""
    for i in nam:
        name += i
    from csv import reader
    opened_file = open(name+".csv")
    read_file = reader(opened_file)
    data = list(read_file)  
    print(data[11])
    scores(data)
except:
    print("Invalid Name")

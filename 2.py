# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:01:25 2019

@author: prajw
"""
def scores(data):
    max1 = 0
    for r in data[1:]:
        runs=0
        if(r[0][-1]=='*'):
            runs=int(r[0][:-1])
        else:
            try:
                runs=int(r[0])
            except:
                runs=0
        if max1 < runs:
            max1 = runs
    max2=0
    for r in data[1:]:
        runs=0
        if(r[0][-1]=='*'):
            runs=int(r[0][:-1])
        else:
            try:
                runs=int(r[0])
            except:
                runs=0
        if runs != max1:
            if max2<runs:
                max2 = runs

                
    print("Max Runs in career "+str(max1))
    print("2nd Highest Runs in career= "+str(max2))
        
    import numpy as np
    import matplotlib.pyplot as plt
    labels=["Runs"]
        
    X=np.arange(len(labels))
    fig,ax = plt.subplots()
    width=0.35
    rects1=ax.bar(X-width/2, max1, width,label='Highest')
    rects2=ax.bar(X+width/2, max2, width, label='Second Hiighest')
    ax.set_ylabel('Scores')
    ax.set_title('Run in overall Career')
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
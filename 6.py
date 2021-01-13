# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:22:41 2019

@author: prajw
"""

def scores(data):
    fif={}
    for r in data[1:]:
        year = r[11][-2:]
        if(year not in fif):
            fif[year]=0
        runs=0
        if(r[0][-1]=='*'):
            runs=int(r[0][:-1])
        else:
            try:
                runs=int(r[0])
            except:
                runs=0
        if runs > 50:
            fif[year]+=1
            
        
        
    import numpy as np
    import matplotlib.pyplot as plt
    labels=[x for x in fif]
    firstHighest=[fif[i] for i in fif]
    
    X=np.arange(len(labels))
    fig,ax = plt.subplots()
    width=0.35
    rects1=ax.bar(X-width/2, firstHighest, width,label='Fifties')
    ax.set_ylabel('Fifties')
    ax.set_title('Years')
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
    scores(data)
except:
    print("Invalid Name")
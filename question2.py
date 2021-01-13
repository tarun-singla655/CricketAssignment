import readData as rd
import matplotlib.pyplot as plt 
import numpy as np
import os

#Name-Akash Karnatak
#Roll No.-B19147
#Branch-Electrical Engineering

def question2(name):
    def secmax(l):
        if len(l)==1:
            return l[0]
        l=set(l)
        l.remove(max(l))
        return max(l)
    files=[]
    X=[]
    Y1=[]
    Y2=[]
    X.append(name)
    playerdata=rd.readData(name)
    playerdata=rd.fixRuns(playerdata)
    runs=[playerdata[i][0] for i in range(len(playerdata))]
    Y1.append(max(runs))
    Y2.append(secmax(runs.copy()))
    xpos=np.arange(len(X))
    plt.xticks(xpos,X,fontsize=7)
    plt.xlabel('Players')
    plt.ylabel('Score')
    width=0.01
    plt.bar(xpos-width/2,Y1,width,label='Highest score')
    plt.bar(xpos+width/2,Y2,width,label='Second highest score')
    plt.ylabel('Runs',fontsize=13)
    plt.xlabel('Players',fontsize=13)
    plt.legend()
    plt.show()

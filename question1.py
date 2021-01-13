import matplotlib.pyplot as plt
import numpy as np
import readData as rd   #import the readData python script to get data of players in a 2-D

#Name-Akash Karnatak
#Roll No.-B19147
#Branch-Electrical Engineering

def question1(name):
    def secmax(l):
        if len(l)==1:
           return 0
        l=set(l)
        l.remove(max(l))
        return max(l)
    playerdata=None
    playerdata=rd.readData(name)
    playerdata=rd.fixYear(playerdata)
    playerdata=rd.fixRuns(playerdata)
    temp_year=playerdata[0][11]
    runs={}                      #dict to store runs in a year
    runs[temp_year]=[]
    for i in range(len(playerdata)):
        run=playerdata[i][0]     #runs scored in a match
        if temp_year==playerdata[i][11]:
            runs[temp_year].append(run)
        else:
            temp_year=playerdata[i][11]
            runs[temp_year]=[run]
    X=list(runs.keys())
    Y1=[max(runs[x]) for x in runs]
    Y2=[secmax(runs[x].copy()) for x in runs]
    x=np.arange(len(X))
    width=0.35
    plt.bar(x-width/2,Y1,width,label='Highest score')
    plt.bar(x+width/2,Y2,width,label='Second highest score')
    plt.xticks(x,X)
    plt.title(name,fontsize=17)
    plt.ylabel('Runs',fontsize=13)
    plt.xlabel('Years',fontsize=13)
    plt.legend()
    plt.show()

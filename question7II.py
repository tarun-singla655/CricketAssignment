import matplotlib.pyplot as plt
import numpy as np
import readData as rd

#Name-
#Roll No.-
#Branch-

def question7II(name):
    playerdata=rd.readData(name)
    out={'Caught Out':0, 'Run Out':0, 'LBW':0, 'Not Out':0, 'Bowled Out':0, 'Stump Out':0, 'Hit wicket':0}
    for i in range(len(playerdata)):
        if playerdata[i][7].strip()=='caught':
            out['Caught Out']+=1
        elif playerdata[i][7].strip()=='run out':
            out['Run Out']+=1
        elif playerdata[i][7].strip()=='lbw':
            out['LBW']+=1
        elif playerdata[i][7].strip()=='not out' or playerdata[i][7].strip()=='retired notout':
            out['Not Out']+=1
        elif playerdata[i][7].strip()=='bowled':
            out['Bowled Out']+=1
        elif playerdata[i][7].strip()=='stumped':
            out['Stump Out']+=1
        elif playerdata[i][7].strip()=='hit wicket':
            out['Hit wicket']+=1
    xpos=np.arange(len(out.keys()))
    X=list(out.keys())
    Y=list(out.values())
    plt.bar(xpos,Y,0.5,align='center')
    plt.title(name,fontsize=17)
    plt.xlabel('Dismissal',fontsize=13)
    plt.xticks(xpos,X)
    plt.show()


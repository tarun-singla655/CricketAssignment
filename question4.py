import matplotlib.pyplot as plt
import numpy as np
import readData as rd
playerdata=None

#Name-
#Roll No.-
#Branch-

def question4(name):
    playerdata=rd.readData(name)
    playerdata=rd.fixYear(playerdata)
    playerdata=rd.fixFours(playerdata)
    temp_year=playerdata[0][11]
    fours={}                      #dict to store fours in a year
    fours[temp_year]=0
    for i in range(len(playerdata)):
        four=playerdata[i][3]     #fours scored in a match
        if temp_year==playerdata[i][11]:
            fours[temp_year]+=four
        else:
            temp_year=playerdata[i][11]
            fours[temp_year]=four
    X=list(fours.keys())
    Y=[fours[x] for x in fours]
    x=np.arange(len(X))
    plt.bar(x,Y,0.5,align='center')
    plt.title(name,fontsize=17)
    plt.xlabel('Years',fontsize=13)
    plt.ylabel('No. of Fours',fontsize=13)
    plt.xticks(x,X)
    plt.show()

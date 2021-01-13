import readData as rd
import matplotlib.pyplot as plt 
import math
import os

#Name-
#Roll No.-
#Branch-

'''
This function calculates the average number
of matches required to score a fifty.
'''
def question7(name):
    playerdata=rd.readData(name)
    playerdata=rd.fixRuns(playerdata)
    fifties=0
    for i in range(len(playerdata)):
        if playerdata[i][0]>=50 and playerdata[i][0]<100:
            fifties+=1
    print(f'{name} scores a fifty on an average after {math.ceil(len(playerdata)/fifties)} matches.')


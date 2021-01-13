import readData as rd
import matplotlib.pyplot as plt 
import numpy as np
import os

#Name-
#Roll No.-
#Branch-

'''
This function returns the number of fours hit 
by a given player in his overall career
'''
def question5(name):
    playerdata=rd.readData(name)
    fours=0
    playerdata=rd.fixFours(playerdata)
    for i in range(len(playerdata)):
        fours+=playerdata[i][3]
    print('\n\n')
    print(f'The number of Fours hit by {name}  in his overall career are {fours}')

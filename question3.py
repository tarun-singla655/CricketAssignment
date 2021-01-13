import readData as rd
import matplotlib.pyplot as plt 
import numpy as np   # import libraries
import os

#Name - Vikash Singh
#Roll No.- B19061
#Branch- Civil engineering 

def question3(name):# name of player
    files=[]
    playerdata=rd.readData(name)        # by name
    playerdata=rd.fixRuns(playerdata)  # this function  fixes the data of runs and then fours
    playerdata=rd.fixFours(playerdata)
    fours=[playerdata[i][3] for i in range(len(playerdata))]  # list comprehension for fours in different matches
    print('\n\n')
    print(f'The maximum number of Fours hit by {name} in an inning (among all innings he has batted) is {max(fours)}')
  # printing maximum of fours using max function
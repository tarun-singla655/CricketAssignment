# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# first 
#import data as d 
#import CricketStats as stat

#Data, Players = d.DataHandling()

def different_teams(data , Player):
    different_teams_names = {}
    l1 = []
    for j in data[1:]:
        
        if j[9][2:] not in l1:
            l1.append(j[9][2:])
        
    return l1
Players = ['HashimAmla','JeanPaulDuminy','JoyRoot','']
nam = input("Enter the name of the player : ").split()  #for sample enter SachinTendulkar
name =""
for i in nam:
    
    name += i
from csv import reader
opened_file = open(name+".csv")
read_file = reader(opened_file)
data = list(read_file)  
print(different_teams(data, name))
# second
def total_runs_team(Data , different_teams_names , Players):
    x1 = input("enter a player to get his runs with different teams")   
    total_runs = {}
        
    for j in different_teams_names.values():
        runs = 0
        for k in Data[x1]:
            if k[9]==j:
                 
                 if(k[0][-1]=='*'):
            runs=int(k[0][:-1])+runs
        else:
            runs=int(k[0])+runs
        total_runs[j] = runs
# third
def total_runs_team(Data , different_teams_names , Players):
    x1 = input("enter a player to get his runs with different teams")   
    total_runs = {}
        
    for j in different_teams_names.values():
        runs = 0
        for k in Data[x1]:
            if k[9]==j:
                 
                 if(k[0][-1]=='*'):
            runs=int(k[0][:-1])+runs
        else:
            runs=int(k[0])+runs
        total_runs[j] = runs     
    
                    
                    
    
        
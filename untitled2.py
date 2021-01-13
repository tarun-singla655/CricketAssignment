import matplotlib.pyplot as plt
import numpy as np
from csv import reader
with open('RossTaylor.csv' ,'r') as t:
    csv_reader = reader(t)
    next(csv_reader)
    maximumruns = 0
    runs = 0
    l1 = []
    year_wise_runs = {}
    for i in csv_reader:
       
        if int(i[11][7:9]) <=20:
            year = "20" + i[11][7:9]
            year = int(year)
        else:
            year = "19" + i[11][7:9]
            year = int(year)
        
        if year not in l1:
            l1.append(year)
            year_wise_runs2[str(year)] = 0
        if i[0][-1]=="*" :
            runs = int(i[0][:-1])

        elif  i[0] == 'DNB' or i[0] =='TDNB':
            continue
        else:
            runs = int(i[0])
        
        if runs > year_wise_runs2[str(year)] and runs < year_wise_runs[str(year)] :
             year_wise_runs2[str(year)] = runs
             
    print(year_wise_runs2)
    
    a4 = list(year_wise_runs2.keys())
    a5 = list(year_wise_runs2.values())
    a6 = np.arange(len(a1))
    plt.bar(a6,a5,tick_label = a4)   
    plt.show()     
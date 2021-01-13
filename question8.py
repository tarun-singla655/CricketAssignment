import numpy as np
import readData as rd

#Name-
#Roll No.-
#Branch-

def question8(name):
    try:
        playerdata=rd.readData(name)
        playerdata = rd.fixRuns(playerdata)
        playerdata=rd.fixYear(playerdata)
    except:
        print('Invalid Input')
    #run is in 1st column, year is in 12th column
    runs=[]
    years = []
    for i in range(len(playerdata)):
        runs.append( playerdata[i][0])
        years.append(playerdata[i][11])

    def total_run_in_a_year(runs,years):
        run_in_a_year ={}
        s=0
        for i in range(len(runs)):
            if i==len(runs)-1:
                s+=runs[i]
                run_in_a_year[years[i]]=s
                break
            if years[i]==years[i+1]:
                s+=runs[i]
                continue
            elif years[i]!=years[i+1]:
                s+=runs[i]
                run_in_a_year[years[i]]=s
                s=0
        return run_in_a_year

    run_in_a_year=total_run_in_a_year(runs,years)
    years=list(run_in_a_year.keys())
    runs =list(run_in_a_year.values())

    def cumulative_run(runs):
        s=0
        runc=[]
        for i in range(len(runs)):
            s+=runs[i]
            runc.append(s)
        return runc
    cum_run =cumulative_run(runs)
    #print(cum_run)
    import matplotlib.pyplot as plt
    plt.title(name,fontsize=17)
    xpos=np.arange(len(years))
    plt.plot(xpos,cum_run,linewidth=3)
    plt.ylabel('Runs',fontsize=13)
    plt.xlabel('Years',fontsize=13)
    plt.xticks(xpos,years)
    plt.show()


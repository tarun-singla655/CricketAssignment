import readData as rd

#Name-
#Roll No.-
#Branch-

def question4II(name):
    try:
        playerdata=rd.readData(name)
        playerdata=rd.fixYear(playerdata)
    except:
        print('Invalid Input')
    total_run_in_a_year ={}
    strike_rate=[]
    years = []
    #print(playerdata)

    for i in range(len(playerdata)):
        if playerdata[i][5]=='-':
            strike_rate.append(0)
        else:
            strike_rate.append( float(playerdata[i][5]))
        years.append(playerdata[i][11])

    def total_strike_in_a_year(strike_rate,years):
        strike_rate_in ={}
        s=0.00
        for i in range(len(strike_rate)):
            if i==len(strike_rate)-1:
                s+=strike_rate[i]
                strike_rate_in[years[i]]=round(s,2)
                break
            if years[i]==years[i+1]:
                s+=strike_rate[i]
                continue
            elif years[i]!=years[i+1]:
                s+=strike_rate[i]
                strike_rate_in[years[i]]=round(s,2)
                s=0.00
        return strike_rate_in
    strike_rate_in_a_year =total_strike_in_a_year(strike_rate,years)
    years=list(strike_rate_in_a_year.keys())
    strike_rate=list(strike_rate_in_a_year.values())

    import matplotlib.pyplot as plt
    import numpy as np
    x=np.arange(len(years))
    plt.bar(x,strike_rate,align = 'center')
    plt.xticks(x,years)
    plt.ylabel('Strike rate',fontsize =13)
    plt.title(name,fontsize=17)
    plt.xlabel('Years',fontsize=13)
    plt.show() 


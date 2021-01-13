import data as d 
import matplotlib.pyplot as plt 
import numpy as np

def AveragreRuns(Player, From = 1951, To = 2019):
    if To is AveragreRuns.__defaults__[1]:
        To = From
    else:
       To = To
    
    From = str(From) + "0101"
    To = str(To) + "1231"
    
    Average = 0
    Count   = 0
    Flag    = 1
    for i in range(1, len(Player)):
        if Player[i][11] >= From and Player[i][11] <= To: 
            if Player[i][0] != 'TDNB' and Player[i][0] != 'DNB': 
                if Player[i][7] == "not out":
                    Flag = 0
                else:
                    Flag = 1
                
                Count = Count + Flag    
                Average = Average + float(Player[i][0])

    if Count > 0:                  #####
        Average = Average/Count
#    print(round(Average,2))
    return Average

        
def YearWiseAverageStat(Player, From = 1951, To = 2019):
    Years = range(From, To+1)
#    print(Years)
    AverageStat = []
    for year in Years:
        AverageStat.append(AveragreRuns(Player, year))
    return(AverageStat)

def AvergeStatAll_Players(Data, Players, From = 1951, To = 2019):
    AvergStat = {}
    for i in range(len(Players)):
        d.CleanRuns(Data[Players[i]])
        d.FixDates(Data[Players[i]])
        AvergStat[Players[i]] = YearWiseAverageStat(Data[Players[i]], From, To)
    return AvergStat


def PlayerNumber(Players):
    for i in range(len(Players)):
        print(i,'\t',Players[i])

def subcategorybar(Years, Items, width=0.8):
    n = len(Items)
    _X = np.arange(len(Years))
    
    for i in range(n):
        plt.bar(_X - width/2. + i/float(n)*width, Items[i][1], width=width/float(n), align="edge",label = Items[i][0])   
    plt.xticks(_X, Years, rotation=90)

    plt.xlabel('Year') 
    plt.ylabel('Average Runs') 
    # plot title 
    plt.title('Stat!') 
    plt.legend()
    FileName = ''
    for i in range(len(Items)):
        if i > 0:
            FileName += '_' + Items[i][0]
        else:
            FileName +=  Items[i][0]
    FileName += '.png' 
    plt.savefig(FileName,dpi = 1000)
    plt.show()
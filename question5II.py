import readData as rd

#Name-
#Roll No.-
#Branch-

def question5II(name):
    playerdata=[]
    try:
        playerdata=rd.readData(name)
        playerdata=rd.fixRuns(playerdata)
    except:
        print('Invalid Input')
    #print(playerdata)

    sum_of_runs = 0
    no_balls=[]
    for i in range(len(playerdata)):
        sum_of_runs+=playerdata[i][0]
        if playerdata[i][2]=='-':
            no_balls.append(0)
        else:
            no_balls.append(int(playerdata[i][2]))
    #for i in no_balls:
    sum_of_balls=sum(no_balls)
    strike_rate = (sum_of_runs/sum_of_balls)*100
    print('\n\n')
    print('Overall career strike rate of '+name+' is',strike_rate)

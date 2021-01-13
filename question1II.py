import readData as rd #import readData to get data of players

#Name-  Tarun singla 
#Roll No.- B19198
#Branch- eleectrical engineering 
# in this quesion 
def question1II(name):  
    def readTeams(playername):  # playername denotes nome of player
        print('\n\n')
        read=open(playername+'.csv','r')  
        read.readline()   # reads first line as it contains heading 
        teams=[]
        for row in read:
            row=row.strip().split(',')  
            teams.append(row[9])
        read.close()
        teams=list(set(teams))    # removes repeated values 
        teams.sort()
        return teams  # return list of teams 
    try:
        teams=readTeams(name)
        print(f'{name} has played against the following teams:')
        for i in teams:
            print( i )   # print teams 
    except:
        print('Error')


import readData as rd

#Name-  Tarun Singla
#Roll No.-  B19198
#Branch- Electrical engineering 

def question2II(name):
    playername=name
    def readTeams(playername): # name of player 
        read=open(playername+'.csv','r')
        read.readline()   # read lines
        teams=[]
        for row in read:
            row=row.strip().split(',')  # strip function remove spaces
            teams.append(row[9])          
        read.close()
        return teams   # differernt teams a player has played
    teams = readTeams(playername)
    def runs_against_teams(playername):
        read=open(playername+'.csv','r')
        read.readline()
        runs=[]
        for row in read:
            row =row.strip().split(',')
            if row[0]=='DNB' or row[0]=='TDNB':    # this basically runs scored by player in every maths
                                                    # considering the player has not played or notout
                runs.append(0)
            elif row[0].endswith('*'):
                runs.append(int(row[0][:-1]))
            else:
                runs.append(int(row[0]))
        return runs
    runs=runs_against_teams(playername)

    def get_runs_stat(teams,runs):
        team_run={}
        for i in range(len(teams)):
            run=0
            for j in range(len(teams)):
                if teams[i]==teams[j]:
                    run+=runs[j]  # adding runs
            team_run[teams[i]]=run 
            run=0
        return team_run   # it returns the dict of total runs scored by player against a team
    team_run=get_runs_stat(teams,runs)
    teams=list(team_run.keys())      # it is list if teams 
    teams.sort()           # sorting 
    print('\n\n')
    for i in teams:
        print(i,':',team_run[i])    # print runs against different teams


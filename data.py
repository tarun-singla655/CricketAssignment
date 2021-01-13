import os
def ReadData(filename = "HashimAmla.csv"):
    mynumbers = []
    PlayerName = []
    with open(filename) as f:
        for line in f:
            mynumbers.append([n for n in line.strip().split(',')])
    for Records in mynumbers:
        try:
            Runs, Mins, BallsFaced, Fours, Sixes, StrikeRate, BattingPosition, DismissalType, Innings, Opposition, Ground, StartDate, ODINo = Records[0], Records[1], Records[2], Records[3], Records[4], Records[5], Records[6], Records[7], Records[8], Records[9], Records[10], Records[11], Records[12]
            MatchStats = [Runs, Mins, BallsFaced, Fours, Sixes, StrikeRate, BattingPosition, DismissalType, Innings, Opposition, Ground, StartDate, ODINo]
            if MatchStats != ['', '', '', '', '', '', '', '', '', '', '', '', '']:
                PlayerName.append(MatchStats)
            #print(MatchStats)
            
            # Do Something with x and y
        except IndexError:
            print("A line in the file doesn't have enough entries.")
            print(PlayerName)
    return PlayerName

def CleanRuns(Player):
    for i in range(1, len(Player)):
        #print(Player[i][7])
        if Player[i][7] == 'not out' or Player[i][7] == 'retired notout':
            Player[i][0] = Player[i][0].replace('*', '')

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

def FixDates(Player):   
    for i in range(1, len(Player)):
        #print(Player[i][11])
        MatchDate = Player[i][11].split('-')

        #print("Length of MatchDate is = ", len(MatchDate))

        #print(MatchDate)
        
        if int(MatchDate[2]) >= 1 and int(MatchDate[2]) <= 20:
            MatchDate[2] =  "20" + MatchDate[2]
        else:
            MatchDate[2] =  "19" + MatchDate[2]
            
        if MatchDate[1]    == 'Jan':
            MatchDate[1]   =  '01' 
        elif MatchDate[1]  == 'Feb':
            MatchDate[1]   =  '02'
        elif MatchDate[1]  == 'Mar':
            MatchDate[1]   =  '03'
        elif MatchDate[1]  == 'Apr':
            MatchDate[1]   =  '04'
        elif MatchDate[1]  == 'May':
            MatchDate[1]   =  '05'
        elif MatchDate[1]  == 'Jun':
            MatchDate[1]   =  '06'
        elif MatchDate[1]  == 'Jul':
            MatchDate[1]   =  '07'
        elif MatchDate[1]  == 'Aug':
            MatchDate[1]   =  '07'
        elif MatchDate[1]  == 'Sep':
            MatchDate[1]   =  '09'
        elif MatchDate[1]  == 'Oct':
            MatchDate[1]   =  '10'
        elif MatchDate[1]  == 'Nov':
            MatchDate[1]   =  '11'
        elif MatchDate[1]  == 'Dec':
            MatchDate[1]   =  '12'

        Player[i][11] = MatchDate[2] + MatchDate[1] + MatchDate[0];

        #print(Player[i])        
    return Player

def DataHandling():
    directory = os.path.join(os.getcwd())
    Players = []
    Data = {}
    for root,dirs,Files in os.walk(directory):
        for file in Files:
           if file.endswith(".csv"):
    #           Data_Files.append(file)
               player = file[0:len(file)-4]
               Players.append(player)
    #           print(player)
               Data[player] = ReadData(file)
    return Data, Players

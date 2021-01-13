import data as d 
import CricketStats as stat

Data, Players = d.DataHandling() # Players is a list contains players name and
                               # Data is a dictionary containg data of players as values and player name as key

print(Data)
print("Comparision")
From = int(input("From year(Between 1951-2019): "))  # starting year
To   = int(input("To year(Between 1951-2019): "))  # Upto

# Dictionary containg list of Average runs per year as values and Player name as key
AvergStatPlayers = stat.AvergeStatAll_Players(Data, Players, From , To)
PlayersAverg = list(AvergStatPlayers.items())

## This function prints the player name and corresponding index in PlayersAverg
stat.PlayerNumber(Players)
## user input
Numbers = list(map(int, input("Enter the player number whose bar chart, you want to plot(comma speration): ").split(',')))
list1 = []
for i in range(len(Numbers)):
    list1.append(PlayersAverg[Numbers[i]])

Years = list(range(From, To+1)) 

stat.subcategorybar(Years, list1) # generates barplot 

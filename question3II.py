import readData as rd

#Name- Vikash Singh
#Roll No.- B19061
#Branch- Civil engineering 

def question3II(name):
    try:
        playerdata=rd.readData(name)   # fix the runs as it contains * and -- values
        playerdata = rd.fixRuns(playerdata)
    except:
        print('Invalid Input')
    def find_no_match():
        count =0   # this functions basically returns  the matches a plated needed to reach 1000
        s=0
        run=1000
        no_of_match=[]
        run_to_be_reached =[]
        for i in range(len(playerdata)):
            s+=playerdata[i][0]  # adding runs 
            count+=1   # adding matches 
            if i==len(playerdata)-1:
                if s>=run:
                    no_of_match.append(count)
                    run_to_be_reached.append(run)   # appending runs till  it reaches 1000
                    break
                elif s<run:
                    break        # this is if the person not able to reach 1000
            elif s>=run:
                no_of_match.append(count)     # it is when a person reaches 1000
                run_to_be_reached.append(run)
                run+=1000
        return no_of_match,run_to_be_reached  # no of matches needed
    no_of_match,run_to_reached = find_no_match()
    import matplotlib.pyplot as plt
    import numpy as np
    x=np.arange(len(run_to_reached))
    plt.bar(x,no_of_match,align = 'center')
    plt.xticks(x,run_to_reached)
    plt.title(name,fontsize=17)
    plt.ylabel('No. of match to be played',fontsize =13)   # ploting no of match needed 
    plt.xlabel('Run to be reached',fontsize=13)
    plt.show()    



import statistics
import csv
import collections


heights_list = []   



with open('mlb_players.csv', newline='') as player_list:

    next(player_list)

    player_reader = csv.reader(player_list)
   
    for row in player_reader:

        height = row[3].strip()
        height = int(height)
        heights_list.append(height)
        
         
    heights_list = sorted(heights_list)
    d = collections.Counter(heights_list)
    

    sorted_keys = sorted(d)

    for key in sorted_keys:
        val = d[key]
        barstring = "*" * val
        print(str(key) + '  ' +barstring)

        
        

    

    
    total = statistics.quantiles(heights_list, n=4, method='exclusive')

    print(total[-1])
    

    

    

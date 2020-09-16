
import statistics
import csv
import collections



with open('mlb_players.csv', newline='') as player_list:

    player_reader = csv.reader(player_list)
    heights = []

    for row in player_reader:
        height = row[4]
        print(height)
        


   
   

    

    

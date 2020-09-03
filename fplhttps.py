import requests
from os import path
import csv
import codecs
###
def headfind(jsn,page):
    headers = []
    for i in jsn[page]:
        for j in i.keys():
            headers.append(j)
        break
    return headers
###
def filemaker(heads,jsn,page):
    with open(page + 'DataSet.csv', 'w',errors = 'IGNORE',newline='') as file:
        writer = csv.DictWriter(file, fieldnames = heads)
        writer.writeheader()
        for i in jsn[page]:
            writer.writerow(i)
        '''
            newrow = {}
            for k,v in i.items(): 
                if k not in heads:
                    pass
                else:
                    if k == "element_type":
                        if v == 4:
                            v = "Forward"
                        elif v == 2:
                            v = "Defender"
                        elif v == 3:
                            v = "Midfielder"
                        else:
                            v = "GoalKeeper"
                    newrow[k] = v
            '''
    return
###
def maker(page):
    out=requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    newj = out.json()
    headers = headfind(newj,page)
    filemaker(headers,newj,page)
###
def main():
    print('''
    --> events
    --> game_settings
    --> phases
    --> teams
    --> total_players
    --> elements
    --> element_stats
    --> element_types
        ''')
    inner = input("What API data would you like to Put (From above): ")
    ##try:
    if path.exists(inner + "DataSet.csv") == True: 
        cho = input("This Data Set has already been made would you like to update it? (y/n): ")
        if cho.rstrip().upper() == "Y":
            maker(inner)
    else:
        maker(inner)
    ###
    #except:
    #    stover = input("That was weird looks like you are retarded would you like to try again? (y/n): ") 
    #    if stover.rstrip().upper() == "Y":
    #        main()
    ###
    print("Done")
###           
if __name__ == "__main__":
    main()
##headers = ['web_name',"now_cost",'total_points','team','element_type','minutes','goals_scored','assists','clean_sheets','goals_conceded','own_goals','penalties_saved','penalties_missed','yellow_cards','red_cards','saves','bonus','bps','influence','                creativity','threat','ict_index','influence_rank','influence_rank_type','creativity_rank','creativity_rank_type','threat_rank','threat_rank_type','ict_index_rank','ict_index_rank_type']


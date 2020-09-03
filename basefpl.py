import requests
import csv
import codecs 
from os import path
###
def headfind(jsn,page):
    headers = []
    try:
        for i in jsn[page]:
            for j in i.keys():
                headers.append(j)
            break    
    except:
        try:
            for i in jsn[page]:
                print(i)
        except:
            print(jsn[page])
    return headers
###
def filemaker(heads,jsn,page):
    with codecs.open( page +'Data.csv', 'w',encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames = heads)
        writer.writeheader()
        for i in jsn[page]:
            writer.writerow(i)
    return
def starter(newj,inner):
    headers = headfind(newj,inner)
    if len(headers) == 0: 
        cho = input("The Text above is the output of that object would you like to try another? (y/n) ")
        if cho.rstrip().upper() == "Y":
            main(newj) 
    else:
        filemaker(headers,newj,inner)

def main(newj):
    for i in newj:
        print("--->",i)
    inner = input("What API data would you like to Put (From above): ")
    if path.exists(inner + "Data.csv") == True: 
        cho = input("This Data Set has already been made would you like to update it? (y/n): ")
        if cho.rstrip().upper() == "Y":
            starter(newj,inner)
    else:
        starter(newj,inner)
###
if __name__ == "__main__":
    out=requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    newj = out.json()
    main(newj)
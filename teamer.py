import csv
''
def check(team,settings,budget,bad):
    x = [float(y["Cost Diff"]) for y in team]
    for i in team:
        if float(i["Cost Diff"]) == min(x):
            settings[i['Postion']] += 1
            budget += float(i["Cost"])
            team.remove(i)
            bad.append(i)
    print("#######################")
    maker(settings,budget,team,bad)
''
def maker(settings,budget,team,bad):
    with open('Predict_Values.csv','r',newline = '') as file:
        data = csv.DictReader(file)
        for i in data:
            if i["Name"] not in [x["Name"] for x in team] and i["Name"] not in [y["Name"] for y in bad]:
                if settings[i["Postion"]] >= 1 and float(i["Predicted Points"]) > 100:
                    if int(i["Cost"]) < budget:
                        team.append(i)
                        budget -= int(i['Cost'])
                        settings[i['Postion']] -= 1
    for k,v in settings.items():
        if v != 0:
            check(team,settings,budget,bad)
    return team,settings,budget,bad
''
def refine(team,budget,bad):
    for t in team:
        for b in bad:
            if float(b['Predicted Points']) > float(t['Predicted Points']) and b["Postion"] == t["Postion"]:
                if (float(b["Cost"]) - float(t["Cost"])) == 0.0: 
                    budget += int(t["Cost"])
                    budget -= int(b["Cost"])
                    team.append(b)
                    team.remove(t)
                    bad.remove(b)
                    bad.append(t)
                    refine(team,budget,bad)
                    break
    return team, bad, budget
''
def start(team,budget,settings,bad):
    team,settings,budget,bad= maker(settings,budget,team,bad)
    team,bad,budget = refine(team,budget,bad)
    print("#######################")
    print("Real Team")
    print('--------------')
    for i in team:
        print(i["Name"],i["Predicted Points"])
    print('#########################')
    print("Bad Team")
    print('--------------')
    for i in bad:
        print(i["Name"],i["Predicted Points"])    
''
if __name__ == "__main__":
        team = []
        budget = 960
        settings = {'1':1,"2":5,"3":5,"4":3}
        badteam = []
        start(team,budget,settings,badteam)

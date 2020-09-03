import requests as rq
import pandas as pd

def pd_to_csv(jsn):
    results = pd.DataFrame.from_dict(jsn)
    print(results.head)
    





if __name__ == "__main__":
    out=rq.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    newj = out.json()
    pd_to_csv(newj)

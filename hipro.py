import csv
import time
with open('elementsData.csv','r',newline = '') as file:
    reader = csv.DictReader(file)
    for i in reader:
        if i["element_type"] == "1":
            if int(i["total_points"]) / int(i["now_cost"]) > 2.7 : 
                print(i['web_name'])

    
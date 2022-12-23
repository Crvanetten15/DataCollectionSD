import requests
import json
import numpy as np
import datetime

def findState(state, data):
    for _ in data:
        if state in _:
            print(_)
'''
https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36/data
'''

CovidData = requests.get("https://data.cdc.gov/api/odata/v4/9mfq-cb36?$top=60000")
CovidDataList = CovidData.json()['value']


CleanData = []
indexes = ['submission_date', 'state', 'tot_cases', 'conf_cases', 'new_case', 'tot_death']
# f.write(str(CovidDataList['value']))
# exit()

for _ in range(len(CovidDataList)):
    tempList = []
    for x in indexes:
        try:
            temporary = CovidDataList[_][x]
        except:
            temporary = None
        tempList.append(temporary)
    tempList[0] = tempList[0][:10]
    CleanData.append(tempList)

CleanData.sort(key=lambda x: datetime.datetime.strptime(x[0], '%Y-%m-%d'))

for x in CleanData:
    print(x)

print('Data Points',len(CleanData))

# findState('OH', CleanData)






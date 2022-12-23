import requests

CovidData = requests.get("https://covidtracking.com/data/download/all-states-history.csv")
print(CovidData.status_code)

# CovidDataList = CovidData.json()
# print(list(CovidDataList))

import requests
import json

IBM_Data_Fetch = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=9XD63JNDBUQX3NEJ'
response = requests.get(IBM_Data_Fetch)
data = response.json()

print(json.dumps(data, indent = 4))
# print(data.keys())
# print(data["Meta Data"])
# print(data["Time Series (5min)"])

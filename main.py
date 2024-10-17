import requests

IBM_data_fetch = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=9XD63JNDBUQX3NEJ'
r = requests.get(IBM_data_fetch)
data = r.json()

print(data)

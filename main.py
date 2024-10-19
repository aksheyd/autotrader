"""Make trades automatically using Nancy Pelosi's stock trades"""
from alphavantage_api.time_series import TimeSeries

def main():
    """Main"""
    symbol = str(input("Enter stock ticker: "))
    time_series = TimeSeries()
    data = time_series.get_time_series_daily(symbol)

    if 'Error Message' in data:
        print("Stock ticker not found!")
    else:
        print(symbol + " stock high on 2024-10-17:",
            data['Time Series (Daily)']['2024-10-17']['2. high'])

if __name__ == '__main__':
    main()

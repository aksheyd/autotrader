"""Make trades automatically using Nancy Pelosi's stock trades"""
from alphavantage_api.time_series import TimeSeries

def main():
    """Main"""
    time_series = TimeSeries()
    symbol = str(input("Enter stock ticker: "))
    date = str(input("Enter trading day you want to analyze, in XXXX-XX(month)-XX(day) format: "))
    data = time_series.get_time_series_daily(symbol)

    if len(date) != 10:
        print("Date is in incorrect format or falls on weekend")
        return
    if 'Error Message' in data:
        print("Stock ticker not found!")
        return

    print(symbol + " stock high on " + date + ":",
        data['Time Series (Daily)'][date]['2. high'])

if __name__ == '__main__':
    main()

"""Make trades automatically using Nancy Pelosi's stock trades"""

from alphavantage_api.time_series import TimeSeries
from alphavantage_api.helper_functions import is_valid_date

def main():
    """Main"""
    time_series = TimeSeries()
    symbol = str(input("Enter stock ticker: "))
    date = str(input("Enter trading day you want to analyze, in YYYY-MM-DD format: "))
    data = time_series.get_time_series_daily(symbol)

    if not is_valid_date(date):
        print("Date is in incorrect format")
        return
    if 'Error Message' in data:
        print("Stock ticker not found!")
        return

    print(symbol + " stock high on " + date + ":",
        data['Time Series (Daily)'][date]['2. high'])

if __name__ == '__main__':
    main()

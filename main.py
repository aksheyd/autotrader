"""Make trades automatically using Nancy Pelosi's stock trades"""

from alphavantage_api.time_series import TimeSeries
from alphavantage_api.helper_functions import is_valid_date
from alphavantage_api.helper_functions import get_date_range

def main():
    """Main"""
    time_series = TimeSeries()
    option = int(input("Enter (1) to analyze trading data from a single days, or (2) to analyze data from a range of dates: "))
    
    if option == 1:
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
    else:
        symbol = str(input("Enter stock ticker: "))
        start_date = str(input("Enter starting date of range, in YYYY-MM-DD format: "))
        end_date = str(input("Enter ending date of range, in YYYY-MM-DD format: "))
        data = time_series.get_time_series_daily(symbol)

        if not is_valid_date(start_date) or not is_valid_date(end_date):
            print("Starting and/or ending date format is incorrect.")
            return
        if 'Error Message' in data:
            print("Stock ticker not found")
            return
        
        dates = get_date_range(start_date, end_date)
        for i in dates:
            print(symbol + " stock high on " + i + ":",
                  data['Time Series (Daily)'][i]['2. high'])

if __name__ == '__main__':
    main()

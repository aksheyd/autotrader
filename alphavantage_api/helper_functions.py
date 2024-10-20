"""Extracts key from config.json and returns URL encoding stock data, used by time_series.py"""

import json
import os
import re
from datetime import datetime, timedelta

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.json')

with open(config_path, encoding='utf-8') as f:
    api_key = json.load(f)['API_KEY']

def create_url(function, symbol):
    """Create a URL for the Alpha Vantage API"""
    return f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'

def is_valid_date(date):
    """Checks if user-inputted date is in correct format for API call"""
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date))

def get_date_range(start_date_str, end_date_str):
    """Incremenents start date until reaches end date"""
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    dates = []
    current_date = start_date

    while current_date <= end_date:
        is_weekend = current_date.weekday() >= 5
        if not is_weekend:
            dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days = 1)

    return dates

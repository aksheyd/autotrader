"""Extracts key from config.json and returns URL encoding stock data, used by time_series.py"""

import json
import os
import re

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

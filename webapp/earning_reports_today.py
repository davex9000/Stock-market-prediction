import requests
import pandas as pd
import datetime

def earning_reports_today():

    # Today's date
    todays_date = datetime.date.today().strftime('%Y-%m-%d')

    # Finnhub API key
    api_key = "cr5r3p1r01qgfrnlm500cr5r3p1r01qgfrnlm50g"

    # API request for today's earnings releases
    url = f"https://finnhub.io/api/v1/calendar/earnings?from={todays_date}&to={todays_date}&token={api_key}"
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()

    earnings_data = data.get('earningsCalendar')

    symbol = [entry['symbol'] for entry in earnings_data]

    return symbol


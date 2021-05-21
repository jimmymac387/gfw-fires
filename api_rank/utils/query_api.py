import time
import requests
from datetime import datetime as dt


BASE_URL = 'https://api.resourcewatch.org/v1/query'

DATA_ID = '1c72bdb6-0f93-4319-bf47-e2f23c5f0e37'    # VIIRS daily change (ADM2)


def date_range_sql(dates):
    """
    Creates SQL snippet from list of date ranges
    Expected format of date list: [(start date, end date, year), ...]
    """
    sql = ""
    i = 0
    
    for start, end, year in dates:
        if i != 0:
            sql += " OR "
        sql += "alert__date >= '" + start.strftime('%Y-%m-%d') + "' AND alert__date <= '" + end.strftime('%Y-%m-%d') + "'"
        i += 1

    return sql


def build_query(iso, dates, printq):
    """
    Creates SQL statement from list of date ranges for specified country
    Expected format of date list: [(start date, end date, year), ...]
    """
    q = (
        "SELECT iso, adm1, adm2, alert__date, SUM(alert__count) " +
        "as alert__count, confidence__cat " +
        "FROM mytable " +
        f"WHERE iso='{iso}' AND confidence__cat='h' AND ({date_range_sql(dates)}) " +
        "GROUP BY iso, adm1, adm2, alert__date"
    )

    if printq:
        print(q)

    return q


def request_params(q):
    """
    Assemble request parameters
    """
    params = {
        'sql': q
    }

    return params


def send_request(country, dates, printq=False):
    """
    Request data from the Resource Watch API
    """
    q = build_query(country, dates, printq)
    p = request_params(q)

    # Turn into try/except statement
    r = requests.get(BASE_URL + '/' + DATA_ID, params=p)
    
    if r.status_code == 200:        
        return r.json()['data']

    else:
        print('Something went wrong...')
        print('Status code: ', r.status_code)
        print('Error message: ', r.json()['errors'][0]['detail'])

    time.sleep(1)
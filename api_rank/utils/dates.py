from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


def date_range_list(days):
    """
    Returns list of date ranges that define the same time period across
    all years in the data
    
    List elements are (start date, end date, year)
    """
    dates = []

    today = dt.today().date()

    for year in range(0, today.year - 2012 + 1):
        start = today - relativedelta(years=year, days=days)
        end = today - relativedelta(years=year)
        yr = end.year
        dates.append((start, end, yr))
    
    return dates
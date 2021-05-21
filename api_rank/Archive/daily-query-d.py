import requests

BASE_URL = 'https://api.resourcewatch.org/v1/query'
DATA_ID = '1c72bdb6-0f93-4319-bf47-e2f23c5f0e37'    # Daily change (ADM2)


# These functions only apply to daily data (need to build out weekly functions)
def select(iso, adm1=None, adm2=None):
    select = "SELECT iso,"
    if adm1:
        select += " adm1,"
    if adm2:
        select += " adm2,"
    select += " alert__date, SUM(alert__count) as alert__count, confidence__cat"
    return select


def where(iso, adm1=None, adm2=None):
    where = f"WHERE iso='{iso}'"
    if adm1:
        where += f" AND adm1={adm1}"
    if adm2:
        where += f" AND adm2={adm2}"
    where += " AND confidence__cat='h'"
    return where


def groupby(iso, adm1=None, adm2=None):
    groupby = "GROUP BY iso,"
    if adm1:
        groupby += " adm1,"
    if adm2:
        groupby += " adm2,"
    groupby += " alert__date"
    return groupby


def build_query(iso, adm1=None, adm2=None, daily=True): # Add adm1 as an optional parameter?
    q = (
        f"{select(iso, adm1, adm2)} " +
        "FROM table " +
        f"{where(iso, adm1, adm2)} " +
        f"{groupby(iso, adm1, adm2)}"
    )
    return q


def query_params(q):
    params = {
        'sql':q
    }
    return params


def send_request(base_url, data_id, iso): 
    q = build_query(iso)
    p = query_params(q)
    r = requests.get(base_url + '/' + data_id, params=p)
    
    if r.status_code == 200:
        return r.json()['data']

    else:
        print('Something went wrong...')
        print('Status code: ', r.status_code)
        print('Error message: ', r.json()['errors'][0]['detail'])


print(build_query('COD', adm1=3, adm2=3))
data = send_request(BASE_URL, DATA_ID, 'COD')
print(data[:2])
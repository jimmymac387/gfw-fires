import requests

BASE_URL = 'https://api.resourcewatch.org/v1/query'
DATA_ID = '1c72bdb6-0f93-4319-bf47-e2f23c5f0e37'    # Daily change (ADM2)


def date_ranges(start_date, end_date):
    pass


# These functions only apply to daily data (need to build out weekly functions)
def build_query(iso, adm1=None, adm2=None, daily=True): # Add adm1 as an optional parameter?
    q = (
        "SELECT iso, adm1, adm2, alert__date, SUM(alert__count) " +
        "as alert__count, confidence__cat " +
        "FROM mytable " +
        f"WHERE iso={iso} AND adm1={adm1} AND confidence__cat='h' AND (alert__date >= '2012-03-01' AND alert__date <= '2016-03-31')" +
        "GROUP BY iso, adm1, alert__date"
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
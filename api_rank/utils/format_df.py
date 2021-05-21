from datetime import datetime as dt
from pandas import DataFrame, to_datetime, Index


def assign_season(date, dates):
    """
    """
    for start, end, year in dates:
        if start <= date <= end:
            return year


def make_df(data, dates):
    """
    """
    df = DataFrame(data)

    df['season'] = (
        to_datetime(df['alert__date'])
            .apply(assign_season, args=(dates, ))
    )

    return df


def adm_filter(df, adm1, adm2):
    if adm1 and adm2:
        return (df['adm1']==adm1) & (df['adm2']==adm2)
    else:
        return (df['adm1']==adm1)


def seasonal_counts(df, adm1, adm2=None):
    filter = adm_filter(df, adm1, adm2)
    i = Index(range(2012, dt.today().year + 1))

    counts = (
        df[filter]
            .groupby('season')
            .agg({'alert__count': 'sum'})
            .reindex(i, fill_value=0)
            # .rename_axis('season')
            # .reset_index()
    )

    return counts


def out_columns(row_list):
    if len(row_list[0]) == 4:
        return ['country', 'adm1', 'current_alerts', 'significance',]
    if len(row_list[0]) == 5:
        return ['country', 'adm1', 'adm2', 'current_alerts', 'significance']


def format_out(row_list):
    columns = out_columns(row_list)

    df = DataFrame(
        row_list,
        columns=columns
    )

    df['score'] = df.significance * df.current_alerts

    return df
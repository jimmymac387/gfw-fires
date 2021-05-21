from datetime import datetime as dt
from utils.format_df import make_df, seasonal_counts, format_out

def calc_std_score(counts):
    x = counts.loc[dt.today().year].item()
    mu = counts['alert__count'].mean().item()
    sd = counts['alert__count'].std().item()

    if sd:
        std_score = (x - mu) / sd
    else:
        std_score = 0
    
    return x, std_score


def std_score_row(df, adm1, adm2=None):
    country = df['iso'][0]
    if adm2:
        counts = seasonal_counts(df, adm1, adm2)
        current_alerts, std_score = calc_std_score(counts)
        return (country, adm1, adm2, current_alerts, std_score) 
    else:
        counts = seasonal_counts(df, adm1)
        current_alerts, std_score = calc_std_score(counts)
        return (country, adm1, current_alerts, std_score) 


def country_std_score(data, dates):
    df = make_df(data, dates)
    regions = df.adm1.unique()
    
    adm1_out = []
    adm2_out = []
    
    for region in regions:
        districts = df[df['adm1']==region].adm2.unique()
        adm1_out.append(std_score_row(df, region))
        
        for district in districts:
            adm2_out.append(std_score_row(df, region, district))
    
    return format_out(adm1_out), format_out(adm2_out)
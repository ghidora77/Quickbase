import pandas as pd
from JSON_Flatten import json_flatten


def get_json():
    # List of the three URLs - Fixed URLs
    lib1 = 'https://asps.leidos.com/webservices/UPG_service.cfc?method=fetch_UPG_JSON&tier=1'
    lib2 = 'https://asps.leidos.com/webservices/UPG_service.cfc?method=fetch_UPG_JSON&tier=2'
    lib3 = 'https://asps.leidos.com/webservices/UPG_service.cfc?method=fetch_UPG_JSON&tier=4'
    json_list = [lib1, lib2, lib3]
    df_list = list()
    for i in json_list:
        n = 1
        df_temp = pd.read_json(i)
        df_temp = json_flatten(df_temp)
        n += 1
        df_list.append(df_temp)
    df = pd.concat(df_list)
    return df


def clean_json(df):
    df.columns = df.columns.str.replace('data.', '')
    df.columns = map(str.title, df.columns)
    df = df.drop(['Recordcount', 'Index'], axis=1)
    df.reset_index(inplace=False)
    return df


def column_rename(df):
    df = df.rename(columns={
        'Datebuilt': 'DateBuilt',
        'Icao': 'ICAO',
        'Nga2_Analyst': 'NGA2_Analyst',
        'Approachtype': 'Approach_Type',
        'Replacementeffectivedate': 'ReplacementEffectiveDate',
        'Last_Eipl_Complete': 'Last_EIPL_Complete',
        'Authoritytype': 'AuthorityType',
        'Cocom': 'COCOM',
        'Nga_Count': 'NGA_Count',
        'Arpt_Name': 'ArptName',
        'Times_Rejected': 'TimesRejected',
        'Replacementfileid': 'ReplacementFileID',
        'QC_Analyst': 'QC_Analyst',
        'Effectiveto': 'EffectiveTo',
        'Nox_Score': 'NOX_Score',
        'Hostfileid': 'HostFileID'
    })
    df.index = range(len(df))
    return df


def BuildLibrary():
    """
    This function will extract the library data from three websites, flatten the
    JSON, clean the dataframe (including simplifying column names) and output 1 relational dataframe. 

    This function will run once every thirty minutes and takes about 10 seconds to run. 
    
    This script will run in full each time. 
    """
    df = get_json()
    df = clean_json(df)
    df = column_rename(df)
    return df

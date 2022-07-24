# Read in relevant libraries
import os
import pandas as pd
from io import StringIO
from f_json_flatten import json_flatten

def BuildLibrary():

    """
    This function will extract all of the library data from the three websites, flatten the
    JSON, clean the dataframe (including simplifying column names) and output 1 relational dataframe. 

    This function will run once per hour and takes about 10 seconds to run. 
    """
    # List of the three URLs
    lib1 = 'https://asps.leidos.com/webservices/UPG_service.cfc?method=fetch_UPG_JSON&tier=1'
    lib2 = 'https://asps.leidos.com/webservices/UPG_service.cfc?method=fetch_UPG_JSON&tier=2'
    lib3 = 'https://asps.leidos.com/webservices/UPG_service.cfc?method=fetch_UPG_JSON&tier=4'
    
    # Package into a list
    json_list = [lib1, lib2, lib3]

    # Loop through the three JSONs 
    # Flatten and put each dataframe into a temporary list
    df_list = list()
    
    for i in json_list:
        n = 1
        df_temp = pd.read_json(i)
        df_temp = json_flatten(df_temp)
        #df_temp['index_1'] = str(n) + '-' + df_temp.index.astype(str)
        n+=1
        df_list.append(df_temp)

    # Consolidate the dataframe = `df`
    df = pd.concat(df_list)
    
    # Strip off the `data.` prefix in column names
    df.columns = df.columns.str.replace('data.', '')

    # All columns title case
    df.columns = map(str.title, df.columns)

    # Columns to Drop
    df = df.drop(['Recordcount', 'Index'], axis = 1)

    df.reset_index(inplace=False)

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
        'Nga_Count': 'NGA_Count',
        'Times_Rejected': 'TimesRejected',
        'Replacementfileid': 'ReplacementFileID',
        'QC_Analyst': 'NGA_Count',
        'Effectiveto': 'EffectiveTo',
        'Nox_Score': 'NOX_Score',
        'Hostfileid': 'HostFileID'
    })

    df.index = range(len(df))

    return df
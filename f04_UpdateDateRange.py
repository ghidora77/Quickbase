# Read in relevant libraries
import os
import datetime
import pandas as pd
from io import StringIO
from f_json_flatten import json_flatten


def UpdateDateRange():
    """
    This function pulls the entire DateRange table, filters the data and 
    outputs a simplified dataframe.

    Note: This will run every minute and update the newest records. 

    The timestamp of the previous run is stored in `PrevRun.txt` 
    This file will update with each run of the data. 
    """

    with open('PrevRun.txt', 'r') as file:
        date_max_str = file.read()

    date_max = datetime.datetime.strptime(date_max_str, '%Y-%m-%d %H:%M:%S')

    date_range = 'https://asps.leidos.com/ziptemp/trackerData.json'

    # Read in and flatten to tabular data frame
    df_DateRange = pd.read_json(date_range)

    # Filter by Status
    value_list = ['Complete', 'Rejected By NGA', 'Accept but Rework']
    boolean_series = df_DateRange.STATUS.isin(value_list)
    df_DateRange = df_DateRange[boolean_series]

    # Convert remaining values to datetime
    df_DateRange["STATUSDATE"] = pd.to_datetime(df_DateRange["STATUSDATE"])

    df_DateRange = df_DateRange.sort_values('STATUSDATE')

    df_DateRange = df_DateRange[(df_DateRange['STATUSDATE'] > date_max)]

    update_max_date = str(df_DateRange.STATUSDATE.max())

    if update_max_date != 'NaT':
        file1 = open("PrevRun.txt","w") 
        file1.truncate()
        file1.write(max_date)
        file1.close()

    return df_DateRange
# Read in relevant libraries
import os
import pandas as pd
from io import StringIO
from f_json_flatten import json_flatten

def BuildDateRange():
    """
    This function pulls the entire DateRange table, filters the data and 
    outputs a simplified dataframe.

    Note: This runs one time to build the entire Date Range. 
    Subsequent runs will only process records that are not in the initial dataframe. 
    """
    date_range = 'https://asps.leidos.com/ziptemp/trackerData.json'

    # Read in and flatten to tabular data frame
    df_DateRange = pd.read_json(date_range)
    df_DateRange = json_flatten(df_DateRange)

    # Filter by Status
    value_list = ['Complete', 'Rejected By NGA', 'Accept but Rework']
    boolean_series = df_DateRange.STATUS.isin(value_list)
    df_DateRange = df_DateRange[boolean_series]

    # Convert remaining values to datetime
    df_DateRange["STATUSDATE"] = pd.to_datetime(df_DateRange["STATUSDATE"])

    df_DateRange.sort_values('STATUSDATE')
    df_DateRange = df_DateRange.drop(['index'], axis = 1)

    return df_DateRange
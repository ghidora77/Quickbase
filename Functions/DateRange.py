import pandas as pd


"""
This is a chain of functions that are used to build the `Date Range` dataset

The two primary functions are
1. `BuildDateRange()` - Builds the full DateRange
2. `AppendDateRange()` - Extracts the data that is new
"""


def get_json():
    URL = 'https://asps.leidos.com/ziptemp/trackerData.json'
    df = pd.read_json(URL)
    return df


def filter_data(df):
    # Filter by Status
    value_list = ['Complete', 'Rejected By NGA', 'Accept but Rework']
    boolean_series = df.STATUS.isin(value_list)
    df = df[boolean_series]
    return df


def cleanDateRange(df):
    # Convert remaining values to datetime
    df["STATUSDATE"] = pd.to_datetime(df["STATUSDATE"])
    df.index = range(len(df))
    return df


def BuildDateRange():
    """
    This function pulls the entire DateRange table, filters the data and 
    outputs a simplified dataframe.

    Note: This runs one time to build the entire Date Range. 
    Subsequent runs will only process records that are not in the initial dataframe. 
    """
    df = get_json()
    df = filter_data(df)
    df = cleanDateRange(df)
    return df

"""
This section tests whether we need to append data to the Quickbase API.

The number of records in previous runs is stored in 
"""


def recordNumPrev():
    with open('../Records_DR.txt', 'r') as file:
        records = file.read()
        records = int(records)
    return records


def recordNumCurr(df):
    length = len(df)
    return length


def recordFlag(prevRecords, currRecords):
    """
    Flag to determine whether new records
    """
    flag = False
    if currRecords > prevRecords:
        flag = True
    return flag


def getAppendData(df, flag, prevRecords):
    """
    If there are new records, extract the new records from the data
    """
    if flag:
        df = df.iloc[prevRecords:]
    return df


def newRecords_DR(currRecords):
    """
    Appends the current records to the records text file
    """
    file1 = open("../Records_DR.txt", "w")
    file1.truncate()
    file1.write(str(currRecords))
    file1.close()


def AppendDateRange():
    df = get_json()
    df = filter_data(df)
    prevRecords = recordNumPrev()
    currRecords = recordNumCurr(df)
    flag = recordFlag(prevRecords, currRecords)
    if flag:
        df = getAppendData(df, flag, prevRecords)
        newRecords_DR(currRecords)
    else:
        df = df.truncate(before=-1, after=-1)
    return df


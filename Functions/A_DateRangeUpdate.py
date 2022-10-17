from DateRange import AppendDateRange
from Dropbox import to_dropbox
import os

"""
This is a consolidation script
1. Builds the Date Range
2. Reads in Dropbox Token
3. Writes data to Dropbox
4. Appends the records to existing Date Range file
"""


df = AppendDateRange()

token = os.environ["DROPBOX"]
path = '/DateRangeUpdate/'
fname = 'DateRangeUpdate.csv'

# Adds records to Dropbox file
to_dropbox(df, path, fname, token)

# Appends records to existing DateRange file
path = '/DateRange/'
fname = 'DateRange.csv'
to_dropbox(df, path, fname, token, 'a')

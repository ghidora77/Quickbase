from DateRange import BuildDateRange
from Dropbox import to_dropbox
import os

"""
This is a consolidation script
1. Builds the Date Range
2. Reads in Dropbox Token
3. Writes data to Dropbox
"""

df = BuildDateRange()

# Builds the entire Date Range dataset
token = os.environ["DROPBOX"]
path = '/DateRange/'
fname = 'DateRange.csv'

to_dropbox(df, path, fname, token)

from DateRange import BuildDateRange
from Dropbox import to_dropbox
from dotenv import load_dotenv
import os
load_dotenv()
"""
This is a consolidation script
1. Builds the Date Range
2. Reads in Dropbox Token
3. Writes data to Dropbox
"""

df = BuildDateRange()

# Builds the entire Date Range dataset
token = os.getenv('DROPBOX_ACCESS_TOKEN')
path = '/DateRange/'
fname = 'DateRange.csv'

to_dropbox(df, path, fname, token)

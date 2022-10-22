from Dropbox import to_dropbox
from Library import BuildLibrary
from dotenv import load_dotenv
import os
load_dotenv()

"""
This is a consolidation script
1. Builds the Library Dataset
2. Reads in Dropbox Token
3. Writes data to Dropbox
"""


df = BuildLibrary()
token = os.getenv('DROPBOX_ACCESS_TOKEN')

path = '/Library/'
fname = 'Library.csv'
# Builds the Library Dataset
to_dropbox(df, path, fname, token)


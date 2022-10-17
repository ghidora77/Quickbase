from Dropbox import to_dropbox
from Library import BuildLibrary
import os

"""
This is a consolidation script
1. Builds the Library Dataset
2. Reads in Dropbox Token
3. Writes data to Dropbox
"""


df = BuildLibrary()
token = os.environ["DROPBOX"]

path = '/Library/'
fname = 'Library.csv'
# Builds the Library Dataset
to_dropbox(df, path, fname, token)


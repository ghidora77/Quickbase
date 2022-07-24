import dropbox
from io import StringIO


def to_dropbox(dataframe, path, filename, token, mode = 'w'):
    """
    This function will upload data into dropbox based on the path and filename given. 

    Note: For the next application we will transition to OneDrive, but this suffices for now
    """

    # Initiate Dropbox API
    dbx = dropbox.Dropbox(token)

    csv_buffer = StringIO()
    dataframe.to_csv(csv_buffer, mode = mode, index=True, index_label='index')

    dbx.files_upload(dataframe.to_csv(index=True, index_label='index').encode(), 
        (path + filename), mode=dropbox.files.WriteMode.overwrite)

    return 'Complete'


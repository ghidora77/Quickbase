import json
import requests

def CreateTables(tableName, description, singleRecordName, pluralRecordName, domain, key, appID):
    """
    `CreateTables` function will create the tables within the specified Quickbase app.

    This is typically run only one time, when starting the app, 
    although it can be used for testing. 
    """

    body = {
        "name": tableName,
        "description": description,
        "singleRecordName": singleRecordName,
        "pluralRecordName": pluralRecordName
    }

    headers = {
        'QB-Realm-Hostname': domain,
        'User-Agent': '{User-Agent}',
        'Authorization': ('QB-USER-TOKEN ' + key)
    }
    params = {
        'appId': appID
    }

    body = body
    r = requests.post(
        'https://api.quickbase.com/v1/tables', 
        params = params, 
        headers = headers, 
        json = body
    )

    return print(json.dumps(r.json(),indent=4))

def DeleteTables(domain, appID, tableID, key):
    """
    `DeleteTables` function will delete the specified table. 
    """

    headers = {
        'QB-Realm-Hostname': domain,
        'User-Agent': '{User-Agent}',
        'Authorization': ('QB-USER-TOKEN ' + key)
    }
    params = {
        'appId': appID
    }
    r = requests.delete(
    ('https://api.quickbase.com/v1/tables/' + tableID), 
    params = params, 
    headers = headers
    )

    return print((json.dumps(r.json(),indent=4)))
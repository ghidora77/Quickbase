import pandas as pd


def json_flatten(df):
    """
    'json_flatten' will flatten out nested JSON data to create a 
    fully relational dataset.

    The input is a dataframe with nested JSON and the output is a dataframe. 
    """
    df = df.reset_index()
    s = (df.applymap(type) == list).all()
    list_columns = s[s].index.tolist()
    s = (df.applymap(type) == dict).all()
    dict_columns = s[s].index.tolist()
    while len(list_columns) > 0 or len(dict_columns) > 0:
        new_columns = []
        for col in dict_columns:
            horiz_exploded = pd.json_normalize(df[col]).add_prefix(f'{col}.')
            horiz_exploded.index = df.index
            df = pd.concat([df, horiz_exploded], axis=1).drop(columns=[col])
            new_columns.extend(horiz_exploded.columns) # inplace
        for col in list_columns:
            df = df.drop(columns=[col]).join(df[col].explode().to_frame())
            new_columns.append(col)
        s = (df[new_columns].applymap(type) == list).all()
        list_columns = s[s].index.tolist()
        s = (df[new_columns].applymap(type) == dict).all()
        dict_columns = s[s].index.tolist()

    return df

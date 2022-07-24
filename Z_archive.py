
"""
### Building Index
The index below (ARPT_NAME, AUTHORITYTYPE, replacementFileId, IDENTIFIER) is pretty clunky for an index. Not sure if that's going to work, being that there's spaces in the airport name and the identifier is empty in most cases.  

I'm not sure how they update this data, and I don't see any patterns in the way the index is built (I can't actually tell if that's a real index or just the numbers that auto-increment), but one thought is to use their existing ID (integers that grow) and put a prefix in front of it (the three libraries start their indices over at 0). It will ensure that they are all unique, and you can always use that data match library to detect exactly where data is modified/data/added. No guarantee, but being that they're using JSON I'd guess they're not doing additions in the middle of the data. 

One other idea is build a join table with the four variables you mention, and create an integer index for each unique value - so `BEN GURION` is index number 1, SANTA LUCIA is index number 2, etc....repeat the process for all variables, so replacementFileID might be an index of 1 for all the empty values, value. It will fit the same concept as using those four variables to build an index, but it will be much more concise. 

You can look at the data below - `index_1`, `index_2` and `index_3`

## Indices

Scroll over all the way to the right - there's index 1, index 2 and index 3, all of them are unique - index 3 is simpler than index 2 while conveying the same information, while index 1 is original index from JSON with a prefix (either 1, 2 or 3). 

Ultimately, it should be the creators of the data to identify this a little better, but those are some possible options for you.

"""

others = [df.AUTHORITYTYPE, df.replacementFileId.astype(str),df.IDENTIFIER]
df['index_2'] = df.ARPT_NAME.str.cat(others, sep ='-')


varnames = ['ARPT_NAME', 'AUTHORITYTYPE', 'replacementFileId', 'IDENTIFIER']

for i in varnames: 
    # Create a series of all the unique values for the variable name
    join_1 = pd.DataFrame(df[i].unique())
    # Create an integer index that is associated with each unique value
    index = pd.DataFrame(range(len(join_1)))
    # Convert to a dataframe
    join_1 = pd.concat([join_1, index], axis = 1)
    # Rename each index 'ID_' plus variable name
    join_1.columns = [i, ( 'ID_' + str(i) )]
    # Merge to original dataframe
    df = df.merge(join_1, how = 'left', left_on = i, right_on = i )

# index_3 has all four variables separated with a '-'
df['index_3'] = (
    df.ID_ARPT_NAME.astype(str) + '-' + 
    df.ID_AUTHORITYTYPE.astype(str) + '-' + 
    df.ID_replacementFileId.astype(str) + '-' + 
    df.ID_IDENTIFIER.astype(str)
    )

df = df.drop(
    ['ID_ARPT_NAME', 
    'ID_AUTHORITYTYPE', 
    'ID_replacementFileId',
    'ID_IDENTIFIER'
    ], 
    axis = 'columns')
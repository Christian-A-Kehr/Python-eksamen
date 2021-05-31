from sklearn import preprocessing 

def row_not_null(df):
    """# Find missing values in the dataframe and drop those rows:"""
    print('rows before drop n/a',len(df))
    bool_matrix = df.isnull() # dataframe with True and False values for each cell in the data
    only_null_filter = bool_matrix.any(axis=1) # is there a True value in any column in each row. returns a pandas Series with index matching index of df dataframe
    df = df[only_null_filter] # show all rows that has one or more null values
    df = df.dropna()
    print('rows after',len(df))
    return df

def char_digit(df):
    """ change char to digit for processing (sklearn)"""
    print('Original df contains rows: '+ (str(len(df))))
    df_no_missing = df.loc[(df['Brændstoftype'] != 'other')]
    print ('if no hybrids og electric cars allowed df: '+ (str(len(df_no_missing))))
    print (df_no_missing['Brændstoftype'].unique())
    #df_no_missing.dtypes
    df = df_no_missing
    label_enc =preprocessing.LabelEncoder()
    df['Brændstoftype'] = label_enc.fit_transform(df['Brændstoftype'].astype(str))
    return df
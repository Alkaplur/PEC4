def breakdown_date(df):
    new_column_month = 'month'
    new_column_year = 'year'
    nulos_en_month = df['month'].isnull().sum()
    print("Valores nulos en 'month':",format(nulos_en_month))

    df[[new_column_year,new_column_month]]=df['month'].str.split('-',expand=True)
    print(df.head(5))
    return (df)

def erase_month(df):
    if df is None:
        print('KK')
    columna_eliminar = "month"
    del df[columna_eliminar]
    print(df.info())
    return (df)

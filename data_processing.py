# Funcion para separar el month del year
def breakdown_date(df):
    # Creo las nueva columnas
    new_column_month = 'month'
    new_column_year = 'year'

    # Verifico los valores nulos
    nulos_en_month = df['month'].isnull().sum()
    print("Valores nulos en 'month':", format(nulos_en_month))

    # Hago la separacion usando el guion para separar los datos
    df[[new_column_year, new_column_month]] = df['month'].str.split('-', expand=True)
    print(df.head(5))
    return df


# Funcion para borrar la columna mes
def erase_month(df):
    # Establezco la columna a eliminar
    columna_eliminar = "month"
    # Borro la columna
    del df[columna_eliminar]
    print(df.info())
    return df

import pandas as pd

# Creo la funcion para cargar los datos
# Recibo solo el path del archivo del arhico
def read_csv(path):
    df = pd.read_csv(path)
    print(df.head(5)) # Muetro primeras 5 lineas
    print(df.info()) #Muestro estructura del df
    return df

def clean_csv(df):
    columns_to_keep = ['month', 'state', 'permit', 'handgun','long_gun']
    df_clean = df.loc[:, columns_to_keep]
    print(df_clean.info())  # Muestro estructura del df
    return (df_clean)

def rename_col(df):
    column = "long_gun"
    new_column = "longgun"
    if column in df.columns:
        df_renamed = df.rename(columns = {column:new_column})
        return (df_renamed)
    else:
        print("La columna {} ya existe".format(new_column))
        return (df)





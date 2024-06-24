import pandas as pd


# Funcion para la agrupacion por state y year
def groupby_state_and_year(df):
    # Columnas por las que se agrupará
    columna_agrupar1 = 'year'
    columna_agrupar2 = 'state'

    # Agrupar por ambas columnas y sumar los valores
    df_grouped = df.groupby(by=[columna_agrupar1, columna_agrupar2]).sum().reset_index()

    # Mostrar las 5 primeras filas del dataframe resultante
    print('La agrupación se realizó correctamente. Primeras 5 filas del dataframe resultante:')
    print(df_grouped.head())
    return df_grouped


# Funcion para mostrar los valores mas altos de handgun
def print_biggest_handguns(df):
    variable_max = 'handgun'  # Confirmo que el nombre de la columna es correcto

    # Calcular el máximo de la variable a buscar por año
    max_by_year = df.groupby('year')[variable_max].max().reset_index()

    # Fusiono con el DataFrame original para obtener los estados correspondientes
    merged_df = pd.merge(df, max_by_year, on=['year', variable_max], how='inner')

    # Mostrar por pantalla los estados con los máximos valores de hand_gun por año
    print(merged_df)


# Funcion para mostrar los valores más altos de longgun
def print_biggest_longguns(df):
    variable_max = 'longgun'  # Confirmo que el nombre de la columna es correcto

    # Calcular el máximo de la variable a buscar por año
    max_by_year = df.groupby('year')[variable_max].max().reset_index()

    # Fusiono con el DataFrame original para obtener los estados correspondientes
    merged_df = pd.merge(df, max_by_year, on=['year', variable_max], how='inner')

    # Mostrar por pantalla los estados con los máximos valores de longgun por año
    print(merged_df)

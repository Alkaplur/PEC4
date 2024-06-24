import pandas as pd


# Funcion para agrupar por estado
def groupby_state(df):

    # Agrupar por estado y sumar los valores
    df_grouped_by_state = df.groupby('state').agg({'longgun': 'sum', 'permit': 'sum', 'handgun': 'sum'}).reset_index()

    # Mostrar las 5 primeras filas del DataFrame resultante
    print('Las primeras 5 filas del DataFrame agrupado por estado y ordenado por ratio:')
    print(df_grouped_by_state.head())

    # Devolver el DataFrame agrupado
    return df_grouped_by_state


# Funcion para hacer la limpieza de datos
def clean_states(df):
    # Definir los valores que deben ser eliminados ya que no contamos con datos
    values_to_remove = ["Guam", "Mariana Islands", "Puerto Rico", "Virgin Islands"]

    # Encontrar los índices de las filas que contienen estos valores
    indices_to_remove = df[df['state'].isin(values_to_remove)].index

    # Eliminar las filas utilizando el método drop
    df_cleaned = df.drop(indices_to_remove)

    return df_cleaned


# Funcion para combindar con datos de poblacion de US
def merge_datasets(df):
    # Importar la función read_csv desde data_handling
    from data_handling import read_csv

    # Definir la ruta del archivo CSV
    file_path = 'Data/us-state-populations.csv'

    # Cargar el archivo CSV
    df_pop = read_csv(file_path)

    # Realizar la fusión de los DataFrames en base a la columna 'state', conservando todas las columnas de df_pop
    df_merged = pd.merge(df, df_pop[['state', 'pop_2014']], how='right', on='state')
    print(df_merged.head(5))
    return df_merged


# Funcion para el calculo de valores relativos
def calculate_relative_values(df):
    # Calculo la relacion entre poblacion y long_gun
    df_relative = df.assign(
        permit_perc=lambda x: x.permit * 100 / x.pop_2014,
        longgun_perc=lambda x: x.longgun * 100 / x.pop_2014,
        handgun_perc=lambda x: x.handgun * 100 / x.pop_2014
    )
    print(df_relative.head(5))
    print(df_relative.describe())
    return df_relative


# Funcion para manejar outlier identificado
def manejar_outlier_kentucky(df):
    # Calcular el promedio de la columna 'permit_perc'
    global_avg_percent = df['permit_perc'].mean().round(2)
    print('La media de permit_perc es', global_avg_percent)

    # Asignar el valor 'Kentucky' a la columna 'State' en la fila 0
    df.loc[0, 'state'] = 'Kentucky'

    # Mostrar el DataFrame actualizado
    print("La informacion del estado de Kentucky es:\n")
    print(df.head(1))

    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = global_avg_percent

    global_avg_percent_udpated = df['permit_perc'].mean().round(2)
    print('La media de permit_perc corregida es', global_avg_percent_udpated)

    respuesta = """
        Se observa una notable reduccion de la media del permit_perc desde 34.88 a 21.07.
        Queda en evidencia por lo tanto que Kentucky era realmente un outlier y su correción 
        permite tener una vision más ajustada a la realidad de esta variable
        """
    print(respuesta)

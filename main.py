# Verifico que estoy trabajando en el main
if __name__ == "__main__":
    # Ejercicio 1.1
    # Importo la función necesaria para la carga
    from data_handling import read_csv
    # Path al arhivo
    file_path = 'Data/nics-firearm-background-checks.csv'
    print('Ejercicio 1.1 - Importo el dataframe\n')
    df = read_csv(file_path)  # llamada a la función de carga

    # Ejercicio 1.2. Limpio los datos llamando a la funcion
    from data_handling import clean_csv

    print()
    print('Ejercicio 1.2. Limpio los datos\n')
    df_clean = clean_csv(df)

    # Ejercicio 1.3. Renombro las columnas y las muestro por pantalla
    from data_handling import rename_col

    print()
    print('Ejercicio 1.3. Renombro columnas\n')
    df_renamed = rename_col(df_clean)
    print(df_renamed.head(5))

    # Ejercicio 2.1. Separo la columna fecha en year y month
    from data_processing import breakdown_date

    print()
    print('Ejercicio 2.1. Divido fecha en month y year\n')
    df_divided = breakdown_date(df_renamed)

    # Ejercicio 2.2. Borro la columna month
    from data_processing import erase_month

    print()
    print('Ejercicio 2.2. Borro la columna month\n')
    df_removed = erase_month(df_divided)

    # Ejercicio 3.1. Agrupo por state y year
    from data_wrangling import groupby_state_and_year

    print()
    print('Ejercicio 3.1. Agrupo los datos por year y state\n')
    df_grouped = groupby_state_and_year(df_removed)

    # Ejercicio 3.2. Muestro valores más altos
    from data_wrangling import print_biggest_handguns

    print()
    print('Ejercicio 3.2. Muestro valores más altos\n')
    print_biggest_handguns(df_grouped)

    # Ejercicio 3.3. Muestro valores más altos
    from data_wrangling import print_biggest_longguns

    print()
    print('Ejercicio 3.3. Muestro valores más altos\n')
    print_biggest_longguns(df_grouped)

    # Ejercicio 4.1. Análisis temporal time_evolution
    from analisis_temporal import time_evolution

    print()
    print('Ejercicio 4.1. Análisis temporal time_evolution\n')
    # Llamo a la funcion y paso el df no agrupado, ya que necesito otra agrupacion
    time_evolution(df_removed)

    # Ejercicio 4.2. Comentario del gráfico
    respuesta = """
    Se observa una correlación entre los permits y los handguns. 
    Los long-guns parecen seguir una tendencia más independiente de los permits, 
    siguiendo una tendencia diferente. Los hand-guns especialmente a partir de 2007
    siguen un patrón muy similar al de los permits. Es evidente que la pandemia supuso
    un notable impacto a las tres variables ya que cayeron a niveles de 2000/01.
    """
    print('Ejercicio 4.2. Comentario del gráfico')
    print(respuesta)

    # Ejercicio 5.1. Agrupación por estados
    from analisis_estados import groupby_state

    print()
    print('Ejercicio 5.1. Agrupación por estados\n')
    df_estado = groupby_state(df_grouped)

    # Ejercicio 5.2. Limpieza de estados
    from analisis_estados import clean_states

    print()
    print('Ejercicio 5.2. Limpieza de estados\n')
    df_estado_clean = clean_states(df_estado)

    # Ejercicio 5.3. Merge de data_sets
    from analisis_estados import merge_datasets

    print()
    print('Ejercicio 5.3. Merge de data_sets\n')
    df_estado_clean_merged = merge_datasets(df_estado)

    # Ejercicio 5.4. Calculo de valores relativos
    from analisis_estados import calculate_relative_values

    print()
    print('Ejercicio 5.4. Calculo de valores relativoss\n')
    df_relative = calculate_relative_values(df_estado_clean_merged)

    # Ejercicio 5.5. Media en info kentucky
    from analisis_estados import manejar_outlier_kentucky

    print()
    print('Ejercicio 5.5. Eliminacion de Outliers - Kentucky\n')

    manejar_outlier_kentucky(df_relative)

    # Ejercicio 6. Elaborar los mapas
    from mapas_Coropleticos import elaborar_mapas

    print()
    print('Ejercicio 5.5. Elaborar mapas\n')
    variables = ("permit_perc", "handgun_perc", "longgun_perc")
    elaborar_mapas(df_relative, variables)

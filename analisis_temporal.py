import matplotlib.pyplot as plt

def time_evolution(df):
    # Agrupar por año y sumar los valores de permit, hand_gun y long_gun
    df_grouped = df.groupby('year')[['permit', 'handgun', 'longgun']].sum().reset_index()

    # Crear el gráfico y ajusto tamaño
    plt.figure(figsize=(10, 6))

    # Muestro cada una de las lineas solicitadas con un punto cada año y la leyenda
    plt.plot(df_grouped['year'], df_grouped['permit'], marker='o', label='Permit')
    plt.plot(df_grouped['year'], df_grouped['handgun'], marker='o', label='Hand Gun')
    plt.plot(df_grouped['year'], df_grouped['longgun'], marker='o', label='Long Gun')

    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title('Evolucion temporal de las variables permit, hand_gun y long_gun registrado')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=90)  # Rotar etiquetas de los años para que se vean bien
    plt.tight_layout()  # Ajustar el diseño para que no se corten las etiquetas
    plt.show()

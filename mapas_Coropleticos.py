import folium
import numpy as np


# Funcion para elaborar los mapas
def elaborar_mapas(df, variables):
    # Rutas
    output_dir = "/Users/davidnogueras/PycharmProjects/PEC4"

    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
    )
    state_geo = f"{url}/us-states.json"

    for variable in variables:
        # Definir los intervalos de colores (ya que cada variable tiene distintos valores)
        min_val = df[variable].min()
        max_val = df[variable].max()
        # Crear los umbrales incluyendo el valor mínimo y máximo
        thresholds = np.linspace(min_val, max_val, num=5)  # Ajuste a 5 umbrales

        print(f"Thresholds: {thresholds} for variable {variable}")  # Añadir un print para verificar los umbrales

        # Crear el mapa
        m = folium.Map(location=[40, -95], zoom_start=4)
        folium.Choropleth(
            geo_data=state_geo,
            name="choropleth",
            data=df,
            columns=["state", variable],
            key_on="feature.properties.name",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.1,
            legend_name=f"{variable.replace('_', ' ').title()} (%)",
            threshold_scale=thresholds.tolist()
        ).add_to(m)

        folium.LayerControl().add_to(m)

        # Guardar el mapa en un archivo específico para cada variable
        output_path = f"{output_dir}/choropleth_map_{variable}.html"
        m.save(output_path)
        print(f"Map for {variable} has been saved as {output_path}. Open this file in a web browser to view the map.")

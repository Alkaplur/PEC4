# Análisis de Datos de Uso de Armas de Fuego en Estados Unidos

Este proyecto realiza un análisis de los datos de uso de armas de fuego en Estados Unidos. Incluye la carga, transformación y análisis básico de los datos, así como la representación gráfica de las proporciones relativas de los permisos y posesión de armas cortas y escopetas por estado.

El proyecto se ha desarrollado en el marco de la asignatura de **Programación para la Ciencia de Datos - Aula 1** de la **Universitat Oberta de Catalunya**.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Contacto](#contacto)

## Instalación

No existen requisitos específicos de instalación del proyecto. Simplemente descarga los archivos y las carpetas de datos desde el repositorio. Puedes usar un IDE como PyCharm para gestionar los distintos módulos que componen el programa.
Existe un repositorio del proyecto en: https://github.com/Alkaplur/PEC4


## Uso

El proyecto contiene un módulo principal denominado `main.py` que realiza las llamadas a las distintas funciones correspondientes a cada ejercicio del enunciado.

### Módulos

1. **data_handling.py**:
    - Carga, limpia y renombra las columnas del dataset.

2. **data_processing.py**:
    - Divide la columna `fecha` en `year` y `month`, y luego elimina la columna `month`.

3. **data_wrangling.py**:
    - Agrupa los datos por `year` y `state`, y muestra los valores más altos de `handguns` y `longguns`.

4. **analisis_temporal.py**:
    - Realiza un análisis temporal de los datos y presenta un gráfico de los permisos, `handguns` y `longguns`, seguido de un análisis.

5. **analisis_estados.py**:
    - Agrupa los valores por estado y realiza una limpieza adicional de datos. Calcula los porcentajes relativos en base a la población de EE.UU. para obtener una información más objetiva.

6. **mapas_Coropleticos.py**:
    - Incluye un análisis gráfico usando mapas coropléticos. Los resultados de permisos, `handguns` y `longguns` se generan en tres archivos HTML.

### Ejecución

Para ejecutar el proyecto, simplemente corre el módulo `main.py`:

```bash
python main.py


## Instalación
dnogueras@uoc.edu

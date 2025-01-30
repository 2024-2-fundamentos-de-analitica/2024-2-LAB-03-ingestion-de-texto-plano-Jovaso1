"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re
def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    def procesar_linea(linea):
        return re.sub(r'\s+', ' ',  linea.strip()).replace('.', '').strip()


    def procesar_encabezado(encabezados):
        return [encabezado.lower().replace(" ", "_") for encabezado in encabezados]


    def procesar_valor(linea, valor_actual):
        split_linea = re.split(r'\s{2,}', linea)
        if split_linea[0].isdigit():
             valores.append( valor_actual[:])
             valor_actual.clear()
             valor_actual.extend([
                int(split_linea[0]),
                int(split_linea[1]),
                float(split_linea[2].split()[0].replace(',', '.'))
            ])
             porcentaje =  linea.find('%')
             valor_actual.append(procesar_linea(linea[porcentaje + 1:]))
        else:
             valor_actual[-1] += " " + procesar_linea(linea)

    with open("files/input/clusters_report.txt") as file:
         lineas = [linea.strip() for linea in file.readlines() if "---" not in linea]

    encabezado = re.split(r"\s{2,}",  lineas[0])
    encabezado[1] += " palabras clave"
    encabezado[2] += " palabras clave"

    valores = []
    valor_actual = encabezado


    for  linea in  lineas[2:]:
        if  linea:
            procesar_valor( linea,  valor_actual)

    valores.append( valor_actual)
    valores[0] = procesar_encabezado( valores[0])
    dataframe = pd.DataFrame(data= valores[1:], columns= valores[0])
    return dataframe

print(pregunta_01())
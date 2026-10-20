#Actividad 13
#Oswaldo Alejandro González Avalos
#222078763
"""Este código utiliza la librería de pandas para leer un archivo excel, ordenando los datos respecto
a su nivel de prioridad y copiándolos en un nuevo archivo excel"""

import pandas as pd

df = pd.read_excel(r"C:\Users\viane\Downloads\pacientes.xlsx")
pacientes = df.to_dict('records')

prioridad_peso = {'ROJO': 1, 'AMARILLO': 2, 'VERDE': 3}

def debe_ir_antes(a, b):
    if prioridad_peso[a['prioridad']] != prioridad_peso[b['prioridad']]:
        return prioridad_peso[a['prioridad']] < prioridad_peso[b['prioridad']]
    return a['espera_min'] < b['espera_min']

def insertion_sort(lista):
    arr = lista.copy()
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and not debe_ir_antes(arr[j], clave):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr

pacientes_ordenados = insertion_sort(pacientes)

df_ordenado = pd.DataFrame(pacientes_ordenados)
df_ordenado.to_excel(r"C:\Users\viane\Downloads\pacientes_ordenados.xlsx", index=False)

print("Se ha generado el archivo 'pacientes_ordenados.xlsx'")
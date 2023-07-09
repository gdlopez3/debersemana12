"""
    Ejemplo del manejo de hilos
"""

import requests
import time
import csv
import threading
import subprocess
import os 

#Se obtienen las paginas web de los hoteles que existen en Atacames.

def obtener_data():
    lista = []
    with open("paginas/hoteles.csv") as archivo:
        lineas = csv.reader(archivo, delimiter='|')

        for row in lineas:
            numero = row[0].strip()
            url = row[1].strip()
            lista.append((numero, url))
    return lista

def worker(numero, url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url))
    pagina = requests.get(url)
    nombre_archivo = f"{numero}.txt"
    ruta_archivo = os.path.join("SALIDA", nombre_archivo)
    with open(ruta_archivo, "w") as archivo:
        archivo.writelines(pagina.text)
    print(f"Archivo guardado: {nombre_archivo}")
    time.sleep(10)
    print("Finalizando %s" % (threading.current_thread().getName()))

for c in obtener_data():
    # Se crea los hilos
    # en la funci�n
    numero = c[0]
    url = c[1]
    hilo1 = threading.Thread(name='navegando...',
                            target=worker,
                            args=(numero, url))
    hilo1.start()

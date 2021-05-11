"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import time
import tracemalloc
import config as cf
import model
import csv
from datetime import datetime

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Funciones para calcular el tiempo

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en kBytes (ej.: 2100.0 kB)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0
    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory




# Inicialización del Catálogo de libros

def init():
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer, user, sentimen, content):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loaduser(analyzer, user)
    loadsentiment(analyzer, sentimen)
    loadcontext(analyzer, content)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory

def loaduser(analyzer, userfile):

    files = cf.data_dir + userfile
    input_file = csv.DictReader(open(files, encoding="utf-8"), delimiter = ",")

    for user in input_file:
        model.adduser(analyzer, user)
    return analyzer

def loadsentiment(analyzer, sentimentfile):

    files = cf.data_dir + sentimentfile
    input_file = csv.DictReader(open(files, encoding="utf-8"), delimiter = ",")

    for sentiment in input_file:
        model.addsentiments(analyzer, sentiment)
    return analyzer

def loadcontext(analyzer, contextfile):

    files = cf.data_dir + contextfile
    input_file = csv.DictReader(open(files, encoding="utf-8"), delimiter = ",")

    for context in input_file:
        model.addcontext(analyzer, context)
        model.adddanceability(analyzer, context)
        model.addenergy(analyzer, context)
        model.addinstrumentalness(analyzer, context)
        model.addliveness(analyzer, context)
        model.addspeechiness(analyzer, context)
        model.addvalence(analyzer, context)
        model.addloudness(analyzer, context)
        model.addtempo(analyzer, context)
        model.addacousticness(analyzer, context)
    return analyzer


# Funciones de consulta sobre el catálogo

def musicSize(analyzer):

    return model.musicSize(analyzer)


def indexHeight(analyzer):
  
    return model.indexHeight(analyzer)


def indexSize(analyzer):

    return model.indexSize(analyzer)


def minKey(analyzer):
 
    return model.minKey(analyzer)


def maxKey(analyzer):

    return model.maxKey(analyzer)

def getArtist(analyzer):

    return model.getArtist(analyzer)





def req1(nombre, val_min, val_max, cont):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    datos = model.req1(nombre, val_min, val_max, cont)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return datos, delta_time, delta_memory
    

def req2(cont, val_min, val_max, val_mind, val_maxd):

    return model.req2(cont, val_min, val_max, val_mind, val_maxd)

def req3(cont, val_min, val_max, val_mint, val_maxt):

    datosInstru = model.req3(cont, val_min, val_max, val_mint, val_maxt)
    #datosTempo = model.req32(datosInstru, val_mint, val_maxt)

    return datosInstru

def agregar_nuevo(nombre, val_min, val_max):
    
    return model.agregar_nuevo(nombre, val_min, val_max, model.diccionario_generos())

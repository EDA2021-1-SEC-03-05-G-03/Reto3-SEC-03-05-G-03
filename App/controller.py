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

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer, user, sentimen, content):

    loaduser(analyzer, user)
    loadsentiment(analyzer, sentimen)
    loadcontext(analyzer, content)
    return analyzer

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
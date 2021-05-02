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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    
    analyzer = {'registros': None,
                'artistas': None,
                'pistas': None 
                }

    analyzer['registros'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['pistas'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareTrackId)

    return analyzer

# Funciones para agregar informacion al catalogo

def addMusicEvent(analyzer, musicEvent):


    lt.addLast(analyzer['registros'], musicEvent)
   

    return analyzer





# Funciones para creacion de datos

def newMusicEvent(musicEvent):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'trackId': None, 'artistId': None}
    entry['trackId'] = m.newMap(numelements= 100000000,
                                     maptype='PROBING',
                                     comparefunction=compareOffenses)
    entry['artistId'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry




# Funciones de consulta

def musicSize(analyzer):

    return lt.size(analyzer['registros'])

def indexHeight(analyzer):
    
    return om.height(analyzer['pistas'])

def indexSize(analyzer):

    return om.size(analyzer['pistas'])

def minKey(analyzer):
  
    return om.minKey(analyzer['pistas'])

def maxKey(analyzer):
 
    return om.maxKey(analyzer['pistas'])


# Funciones utilizadas para comparar elementos dentro de una lista

def compareIds(id1, id2):

    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareTrackId(tId1, tId2):

    if (tId1 == tId2):
        return 0
    elif tId1 > tId2:
        return 1
    else:
        return -1


# Funciones de ordenamiento
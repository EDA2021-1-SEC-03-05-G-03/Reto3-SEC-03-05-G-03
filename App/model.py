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
    
    analyzer = {'events': None,
                'sentiments': None,
                'user_track': None,
                "context_content": None 
                }

    analyzer['events'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['sentiments'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['user_track'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['context_content'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)

    return analyzer

# Funciones para agregar informacion al catalogo

def addsentiments(analyzer, sentiment):

    om.put(analyzer["sentiments"], sentiment["hashtag"], sentiment)

def adduser(analyzer, user):

    contiene = om.contains(analyzer["user_track"], user["track_id"])

    if not contiene:
        lista = lt.newList()
        lt.addLast(lista, user)
        om.put(analyzer["user_track"], user["track_id"], lista)
    
    else:
        obtener = om.get(analyzer["user_track"], user["track_id"])
        valores = me.getValue(obtener)
        lt.addLast(valores, user)

def addcontext(analyzer, context):

    contiene = om.contains(analyzer["context_content"], context["artist_id"])
    lt.addLast(analyzer["events"], context)

    if contiene == False:
        lista = lt.newList()
        lt.addLast(lista, context)
        om.put(analyzer["context_content"], context["artist_id"], lista)

    else:
        valor = om.get(analyzer["context_content"], context["artist_id"])
        listaNew = me.getValue(valor)
        lt.addLast(listaNew, context)




# Funciones para creacion de datos

def newMusicEvent(musicEvent):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'trackId': None, 'artistId': None}
    entry['trackId'] = mp.newMap(numelements= 100000000,
                                     maptype='PROBING',
                                     comparefunction=compareIds(id1, id2))
    entry['artistId'] = lt.newList('SINGLE_LINKED', compareTrackId(tId1, tId2))
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

def getArtist(analyzer):

    return om.get(analyzer["pistas"], "user_id")


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

def diccionario_generos():
    dicc = {"Reggae": (60, 90),
            "Down-tempo": (70, 100),
            "Chill-out": (90, 120),
            "Hip-hop": (85, 115),
            "Jazz and Funk": (120, 125),
            "Pop": (100, 130),
            "R&B": (60, 90),
            "Rock": (60, 90),
            "Metal": (60, 90)}
    return dicc


def agregar_nuevo(nombre, val_min, val_max, dic):
    dic[nombre] = (val_min, val_max)
    return dic
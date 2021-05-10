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

from DISClib.DataStructures import linkedlistiterator as it
from DISClib.DataStructures import orderedmapstructure as mo
import config as cf
import random
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
                "context_content": None,
                "track_ids":None,
                "danceability":None,
                "energy":None,
                "instrumentalness":None,
                "liveness":None,
                "speechiness":None,
                "valence":None,
                "loudness":None,
                "tempo":None,
                "acousticness":None,
                }

    analyzer['events'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['sentiments'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['user_track'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['context_content'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['track_ids'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['danceability'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIdsNum)
    analyzer['energy'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIdsNum)
    analyzer['instrumentalness'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIdsNum)
    analyzer['liveness'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['speechiness'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['valence'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['loudness'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['tempo'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareIds)
    analyzer['acousticness'] = om.newMap(omaptype='RBT',
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
    
def adddanceability(analyzer, context):

    contiene = om.contains(analyzer["danceability"], context["danceability"])

    if not contiene:
        lista = lt.newList()
        lt.addLast(lista, context)
        om.put(analyzer["danceability"], context["danceability"], lista)
    
    else:
        obtener = om.get(analyzer["danceability"], context["danceability"])
        valores = me.getValue(obtener)
        lt.addLast(valores, context)

def addenergy(analyzer, context):

    contiene = om.contains(analyzer["energy"], context["energy"])

    if not contiene:
        lista = lt.newList()
        lt.addLast(lista, context)
        om.put(analyzer["energy"], context["energy"], lista)
    
    else:
        obtener = om.get(analyzer["energy"], context["energy"])
        valores = me.getValue(obtener)
        lt.addLast(valores, context)

def addinstrumentalness(analyzer, context):

    contiene = om.contains(analyzer["instrumentalness"], context["instrumentalness"])

    if not contiene:
        lista = lt.newList()
        lt.addLast(lista, context)
        om.put(analyzer["instrumentalness"], context["instrumentalness"], lista)
    
    else:
        obtener = om.get(analyzer["instrumentalness"], context["instrumentalness"])
        valores = me.getValue(obtener)
        lt.addLast(valores, context)

def addliveness(analyzer, context):

    contiene = om.contains(analyzer["liveness"], context["liveness"])

    if not contiene:
        lista = lt.newList()
        lt.addLast(lista, context)
        om.put(analyzer["liveness"], context["liveness"], lista)
    
    else:
        obtener = om.get(analyzer["liveness"], context["liveness"])
        valores = me.getValue(obtener)
        lt.addLast(valores, context)

def addspeechiness(analyzer, context):

    contiene = om.contains(analyzer["speechiness"], context["speechiness"])

    if not contiene:
        lista = lt.newList()
        lt.addLast(lista, context)
        om.put(analyzer["speechiness"], context["speechiness"], lista)
    
    else:
        obtener = om.get(analyzer["speechiness"], context["speechiness"])
        valores = me.getValue(obtener)
        lt.addLast(valores, context)

def addvalence(analyzer, context):

    contiene = om.contains(analyzer["valence"], context["valence"])

    if not contiene:
        lista = lt.newList()
        lt.addLast(lista, context)
        om.put(analyzer["valence"], context["valence"], lista)
    
    else:
        obtener = om.get(analyzer["valence"], context["valence"])
        valores = me.getValue(obtener)
        lt.addLast(valores, context)

def addloudness(analyzer, context):

    contiene = om.contains(analyzer["loudness"], context["loudness"])

    if not contiene:
        lista = lt.newList()
        lt.addLast(lista, context)
        om.put(analyzer["loudness"], context["loudness"], lista)
    
    else:
        obtener = om.get(analyzer["loudness"], context["loudness"])
        valores = me.getValue(obtener)
        lt.addLast(valores, context)

def addtempo(analyzer, context):

    contiene = om.contains(analyzer["tempo"], context["tempo"])

    if not contiene:
        lista = lt.newList()
        lt.addLast(lista, context)
        om.put(analyzer["tempo"], context["tempo"], lista)
    
    else:
        obtener = om.get(analyzer["tempo"], context["tempo"])
        valores = me.getValue(obtener)
        lt.addLast(valores, context)

def addacousticness(analyzer, context):

    contiene = om.contains(analyzer["acousticness"], context["acousticness"])

    if not contiene:
        lista = lt.newList()
        lt.addLast(lista, context)
        om.put(analyzer["acousticness"], context["acousticness"], lista)
    
    else:
        obtener = om.get(analyzer["acousticness"], context["acousticness"])
        valores = me.getValue(obtener)
        lt.addLast(valores, context)




# Funciones para creacion de datos

def newMusicEvent(musicEvent):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'trackId': None, 'artistId': None}
    entry['trackId'] = mp.newMap(numelements= 100000000,
                                     maptype='RBT',
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

    if id1 == id2:
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareIdsNum(id1, id2):

    if float(id1 == id2):
        return 0
    elif float(id1) > float(id2):
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


# Funciones de los requerimientos


#Req 1

def req1(nombre, val_min, val_max, cont):
    lista = []
    datos = om.values(cont[nombre], val_min, val_max)
    contador = 0
    artistas = 0

    for i in lt.iterator(datos):
        for j in lt.iterator(i):
            contador += 1
            for key, value in j.items():
                #print(key, value)
                if key == "artist_id":
                    lista.append(value)
                    
    lista = list(set(lista))
    artistas = len(lista)
    dupla = (contador, artistas)
    return dupla

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Req 2

#intento interno JJ
def req2( cont, val_min, val_max, val_mind, val_maxd): 
    lista = []
    lista2 = []
    energy = om.values(cont["energy"], val_min, val_max)
    dance = om.values(cont["danceability"], val_mind, val_maxd)
    contador = 0
    contador2 = 0
    for i in lt.iterator(energy):
        for j in lt.iterator(i):
            contador += 1
            for key, value in j.items():
                #print(key, value)
                if key == "track_ids":
                    lista.append(value)
    for i in lt.iterator(dance):
        for j in lt.iterator(i):
            contador2 += 1
            for key, value in j.items():
                #print(key, value)
                if key == "track_ids":
                    lista2.append(value)             
    lista = list(set(lista))
    lista2 = list(set(lista2))
    largo = len(lista)
    largo2 = len(lista2)
    cinco = lt.subList(lista2, random.randint(1, float(contador)), 10)
    return cinco


#intento interno
def req2( cont, val_min, val_max, val_mind, val_maxd): 
    lista = []
    lista2 = []
    energy = om.values(cont["energy"], val_min, val_max)
    dance = om.values(cont["danceability"], val_mind, val_maxd)
    contador = 0
    for i in lt.iterator(energy):
        for j in lt.iterator(i):
            contador += 1
            datos = mp.get(j, "energy")
            valor = me.getValue(datos)
            track = mp.get(j, "track_ids")
            id = me.getValue(track)
            if float(valor) >= float(val_min) and float(valor) <= float(val_max):
                if lt.isPresent(lista, id) == 0:
                    lt.addLast(lista, id) 
                    lt.addLast(lista2, j)
    for i in lt.iterator(dance):
        for j in lt.iterator(i):
            contador += 1
            datos = mp.get(j, "danceability")
            valord = me.getValue(datos)
            trackd = mp.get(j, "track_ids")
            idd = me.getValue(trackd)
            if float(valord) >= float(val_mind) and float(valord) <= float(val_maxd):
                if lt.isPresent(lista, idd) == 0:
                    lt.addLast(lista, idd) 
                    lt.addLast(lista2, j)
    return lista2

#intento externo 2
def req2( cont, val_min, val_max, val_mind, val_maxd): 
    energy = om.values(cont["energy"], val_min, val_max)
    dance = om.values(cont["danceability"], val_mind, val_maxd)
    new = it.newIterator(energy)
    lst = lt.newList("SINGLE_LINKED")
    paaa = lt.newList("SINGLE_LINKED")
    while it.hasNext(new):
        l=it.next(new)
        nuevo = it.newIterator(l)
        while it.hasNext(nuevo):
            pedazo = it.next(nuevo)
            ax = mp.get(pedazo, "energy")
            nex = mp.get(pedazo, "track_ids")
            tax = me.getValue(ax)
            fex = me.getValue(nex)
            if float(tax) >= float(val_min) and float(tax) <= float(val_max):
                if lt.isPresent(lst, fex) == 0:
                    lt.addLast(paaa, pedazo)
                    lt.addLast(lst, fex)
    new = it.newIterator(dance)
    while it.hasNext(new):
        l=it.next(new)
        nuevo = it.newIterator(l)
        while it.hasNext(nuevo):
            pedazo = it.next(nuevo)
            ax = mp.get(pedazo, "danceability")
            yex = mp.get(pedazo, "track_ids")
            tax = me.getValue(ax)
            tex = me.getValue(yex)
            if float(tax) >= float(val_mind) and float(tax) <= float(val_maxd):
                if lt.isPresent(lst, tex) == 0:
                    lt.addLast(paaa, pedazo)
                    lt.addLast(lst, tex)
    return paaa



#------------------------------------------------------------------------------------------------------------------------------------------------------------



# Req 4

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
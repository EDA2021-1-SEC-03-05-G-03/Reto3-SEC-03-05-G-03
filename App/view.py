"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

user = "user_track_hashtag_timestamp-small.csv"
sentimen = "sentiment_values.csv"
content = "context_content_features-small.csv"
cont = None

#El total de registros de eventos de escucha cargados
#Total de artistas unicos cargados
#Total de pistas de audio cargadas
#Mostrar los primeros y ultimos 5 eventos de escucha cargados con sus caracteristicas

def printMenu():
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Caracterizar las reproducciones    - Req 1")
    print("3- Encontrar musica para festejar     - Req 2")
    print("3- Encontrar musica para estudiar     - Req 3")
    print("4- Canciones por genero en un rango   - Req 4")
    print("5- Agregar un nuevo genero musical    - Req 4-2")
    print("6- Genero mas escuchado en un tiempo  - Req 5")


def retornar5(analyzer):
    for i in range(0, 5):
        print(lt.getElement(analyzer["events"], i))
    j = 0

    while j <= 4:
        print(lt.getElement(analyzer["events"], lt.size(analyzer["events"]) - j))
        j += 1


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')


    if int(inputs[0]) == 1:
        print("\nCargando información de los archivos ....")
        cont = controller.init()
        cont = controller.loadData(cont, user, sentimen, content)
        print('Numero de eventos: ' + str(lt.size(cont["events"])))

        valores = om.keySet(cont["context_content"])
        print('Numero de artistas: ' + str(lt.size(valores)))

        valor = om.keySet(cont["user_track"])
        print('Numero de pistas: ' + str(lt.size(valor)))

        #rint(retornar5(cont))
        for i in range(0, 5):
            print(lt.getElement(cont["events"], i))
            j = 0

        while j <= 4:
            print(lt.getElement(cont["events"], lt.size(cont["events"]) - j))
            j += 1


    elif int(inputs[0]) == 2:
        pass


    elif int(inputs[0]) == 3:
        pass


    elif int(inputs[0]) == 4:
        pass


    elif int(inputs[0]) == 5:
        
        nombre = str(input("Ingrese el nombre del nuevo genero: "))
        val_min = int(input("Ingrese el valor minimo del Tempo: "))
        val_max = int(input("Ingrese el valor maximo del Tempo: "))

        print(controller.agregar_nuevo(nombre, val_min, val_max))


    elif int(inputs[0]) == 6:
        pass


    else:
        sys.exit(0)




sys.exit(0)
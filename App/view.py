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

user = "user_track_hashtag_timestamp-10pct.csv"
sentimen = "sentiment_values.csv"
content = "context_content_features-10pct.csv"
cont = None

def loadData(cont, user, sentimen, content):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(cont, user, sentimen, content)


def printMenu():
    print("\nBienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Caracterizar las reproducciones    - Req 1")
    print("2- Encontrar musica para festejar     - Req 2")
    print("3- Encontrar musica para estudiar     - Req 3")
    print("4- Canciones por genero en un rango   - Req 4")
    print("5- Agregar un nuevo genero musical    - Req 4-2")
    print("6- Genero mas escuchado en un tiempo  - Req 5")


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')


    if int(inputs[0]) == 0:
        print("\nCargando información de los archivos ...")
        cont = controller.init()
        loadData(cont, user, sentimen, content)

        print('Numero de eventos: ' + str(lt.size(cont["events"])))

        valores = om.keySet(cont["context_content"])
        print('Numero de artistas: ' + str(lt.size(valores)))

        valor = om.keySet(cont["user_track"])
        print('Numero de pistas: ' + str(lt.size(valor)))

        for i in range(1, 6):
            print(lt.getElement(cont["events"], i))
            j = 0

        while j <= 5:
            print(lt.getElement(cont["events"], lt.size(cont["events"]) - j))
            j += 1

        # Calcular tiempo
        answer = controller.loadData(cont, user, sentimen, content)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
               "Memoria [kB]: ", f"{answer[1]:.3f}")


    elif int(inputs[0]) == 1:

        nombre = str(input("Ingrese el nombre de la caracteristica: "))
        val_min = float(input("Ingrese el valor minimo de la caracteristica: "))
        val_max = float(input("Ingrese el valor maximo de la caracteristica: "))

        datos = controller.req1(nombre, val_min, val_max, cont)

        print(nombre +" entre ",val_min ," y ",val_max)
        print("Total de reproducciones: ",datos[0][0]  , " Total de artistas unicos: ",datos[0][1])


        print("Tiempo [ms]: ", f"{datos[1]:.3f}", "  ||  ",
               "Memoria [kB]: ", f"{datos[2]:.3f}")


    elif int(inputs[0]) == 2:

        val_min = float(input("Ingrese el valor minimo de Energy: "))
        val_max = float(input("Ingrese el valor maximo de Energy: "))
        val_mind = float(input("Ingrese el valor minimo de Danceability: "))
        val_maxd = float(input("Ingrese el valor maximo de Danceability: "))

        datos = controller.req2(cont, val_min, val_max, val_mind, val_maxd)

        print("Energy entre ",val_min ," y ",val_max)
        print("Danceability entre ",val_mind ," y ",val_maxd)
        print("Total de tracks unicos: ",datos[0][1])

        print("Track 1: ", datos[0][0][0])
        print("Track 2: ", datos[0][0][1])
        print("Track 3: ", datos[0][0][2])
        print("Track 4: ", datos[0][0][3])
        print("Track 5: ", datos[0][0][4])


        print("Tiempo [ms]: ", f"{datos[1]:.3f}", "  ||  ",
               "Memoria [kB]: ", f"{datos[2]:.3f}")


    elif int(inputs[0]) == 3:

        val_min = float(input("Ingrese el valor minimo del rango de Instrumentalness: "))
        val_max = float(input("Ingrese el valor maximo del rango de Instrumentalness: "))
        val_mint = float(input("Ingrese el valor minimo del rango de Tempo: "))
        val_maxt = float(input("Ingrese el valor maximo del rango de Tempo: "))

        datos = controller.req3(cont, val_min, val_max, val_mint, val_maxt)

        print("Instrumentalness entre ",val_min ," y ",val_max)
        print("Tempo entre ",val_mind ," y ",val_maxd)
        print("Total de tracks unicos: ",datos[0][1])

        print("Track 1: ", datos[0][0][0])
        print("Track 2: ", datos[0][0][1])
        print("Track 3: ", datos[0][0][2])
        print("Track 4: ", datos[0][0][3])
        print("Track 5: ", datos[0][0][4])


        print("Tiempo [ms]: ", f"{datos[1]:.3f}", "  ||  ",
               "Memoria [kB]: ", f"{datos[2]:.3f}")
        

    elif int(inputs[0]) == 4:
        
        nombre = str(input("Ingrese el nombre del genero: "))
        

    elif int(inputs[0]) == 5:
        
        nombre = str(input("Ingrese el nombre del nuevo genero: "))
        val_min = int(input("Ingrese el valor minimo del Tempo: "))
        val_max = int(input("Ingrese el valor maximo del Tempo: "))

        datos = controller.agregar_nuevo(nombre, val_min, val_max)
        print(datos[0])


        print("Tiempo [ms]: ", f"{datos[1]:.3f}", "  ||  ",
               "Memoria [kB]: ", f"{datos[2]:.3f}")


    elif int(inputs[0]) == 6:

        val_min = int(input("Ingrese el valor minimo de la hora: "))
        val_max = int(input("Ingrese el valor maximo de la hora: "))


    else:
        sys.exit(0)




sys.exit(0)
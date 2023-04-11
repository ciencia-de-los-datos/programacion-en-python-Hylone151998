"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

archivo=open("data.csv","r").readlines()
archivo = [z.replace('\n', '') for z in archivo]
archivo = [line.split('\t') for line in archivo]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma=0
    archivo=open("data.csv","r").readlines()
    for lines in archivo:
        lines=lines.split('\t')
        suma= suma + int(lines[1])
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import re
    archivo=open("data.csv","r")
    archivoCompleto=archivo.readlines()
    diccionario={}
    matriz=[]

    for linea in archivoCompleto:
        matriz.append(re.split(",|\t",linea))



    for linea in matriz:
        value=linea[0]
        if value in diccionario:
            diccionario[value]+=1
        else:
            diccionario[value]=1
    diccionario_ordenado=sorted(diccionario.items())
    diccionario_ordenado
    return diccionario_ordenado


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import re
    archivo=open("data.csv","r")
    archivoCompleto=archivo.readlines()
    diccionario={}
    matriz=[]

    for linea in archivoCompleto:
        matriz.append(re.split(",|\t",linea))

    for linea in matriz:
        key=linea[0]
        value=int(linea[1])
        if key in diccionario:
            diccionario[key]+=value
        else:
            diccionario[key]=value
    diccionario_ordenado=sorted(diccionario.items())
    diccionario_ordenado

    
    return diccionario_ordenado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import re
    archivo=open("data.csv","r")
    archivoCompleto=archivo.readlines()
    diccionario={}
    matriz=[]

    for linea in archivoCompleto:
        matriz.append(re.split(",|\t",linea))

    for linea in matriz:
        key=linea[2].split("-")[1]
  

        if key in diccionario:
            diccionario[key]+=1
        else:
            diccionario[key]=1
    diccionario_ordenado=sorted(diccionario.items())
    diccionario_ordenado
    return diccionario_ordenado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data=open("data.csv","r").readlines()
    dictionary= {}  
    for line in data:
        line=line.split('\t')
        letters=line[0]
        nums= line[1]
        for letter, num in zip(letters, nums):
            if letter in dictionary:
                if int(num) > int(dictionary[letter][0]):
                    dictionary[letter]=(int(num),dictionary[letter][1])
                elif int(num) < int(dictionary[letter][1]):  
                    dictionary[letter]=(dictionary[letter][0],int(num))
            else:
                dictionary[letter]=(int(num),int(num))
    lista=[(letter,dictionary[letter][0], dictionary[letter][1])for letter in dictionary]

    resultado=sorted(lista)




    return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import re
    archivo = open("data.csv","r")
    archivoCompleto = archivo.readlines()
    diccionario = {}
    matriz = []

    for linea in archivoCompleto:
        matriz.append(linea.split("\t"))

    for linea in matriz:
        data = linea[4].split(",")
        for element in data:
            key, value = element.split(":")
            value = int(value)  
            if key not in diccionario:
                diccionario[key] = (value, value)
            else:
                current_min, current_max = diccionario[key]
                diccionario[key] = (min(current_min, value), max(current_max, value))

    diccionario_ordenado = sorted(diccionario.items())
    dic_final = []
    for val in diccionario_ordenado:
        dic_final.append([val[0], val[1][0], val[1][1]])



    dic_final = []
    for val in diccionario_ordenado:
        dic_final.append([val[0], val[1][0], val[1][1]])

    dic_final = list(map(tuple, dic_final))
    return dic_final


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    # import re
    # archivo=open("data.csv","r")
    # archivoCompleto=archivo.readlines()
    # diccionario={}
    # matriz=[]

    # for linea in archivoCompleto:
    #     matriz.append(linea.split("\t"))

    # for linea in matriz:
    #     clave=int(linea[1])
    #     valor=linea[0]  
    # if clave not in diccionario:
    #     diccionario[clave]=[valor]
    
    # else:
    #     diccionario[clave].append(valor)
    # diccionario_ordenado=sorted(diccionario.items())
    # print("hola")
    # print(diccionario_ordenado)
    valores = {}
    for row in archivo:
        letra = row[0]
        valor = float(row[1])
        if valor in valores:
            valores[valor].append(letra)
        else:
            valores[valor] = [letra]
 
    return sorted(valores.items())
  

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    
    valores = {}
    for row in archivo:
        letra = row[0]
        valor = float(row[1])
        if valor in valores:
            valores[valor].append(letra)
        else:
            valores[valor] = [letra]
    tuplas = [(valor, sorted(list(set(valores[valor])))) for valor in valores.keys()]
    tup=sorted(tuplas)
    return tup

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    # import re
    # archivo=open("data.csv","r")
    # archivoCompleto=archivo.readlines()
    # diccionario={}
    # matriz=[]

    # for linea in archivoCompleto:
    #     matriz.append(linea.split("\t"))



    # for linea in matriz:
    #     data=linea[4].split(",")

    # for element in data:
    #     key,value=element.split(":")
    #     value=int(value)  
    #     if key not in diccionario:
    #         diccionario[key]=1
    #     else:
    #         diccionario[key]+=1
    # diccionario_ordenado=sorted(diccionario.items())

    # diccionario_ordenado=dict(diccionario_ordenado)
    # diccionario_ordenado

    valores = {}
    for row in archivo:
        diccionario = dict(item.split(':') for item in row[4].split(','))
        for clave in diccionario.keys():
            if clave in valores:
                valores[clave] += 1
            else:
                valores[clave] = 1
    result= dict(sorted(valores.items()))
    return result
    


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    import re
    archivo=open("data.csv","r")
    archivoCompleto=archivo.readlines()
    lista=[]
    matriz=[]

    for linea in archivoCompleto:
        matriz.append(linea.split("\t"))


    for linea in matriz:
        key=linea[0]
        LongCol4=len(linea[3].split(","))
        LongCol5=len(linea[4].split(","))
        lista.append((key,LongCol4,LongCol5))
    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    

    """
    
   
    data=open("data.csv","r").readlines()
    dictionary={}
    new_dictionary={}
    for line in data:
      line=line.strip().split('\t')
      letter=line[3].split(",")
      num=int(line[1])
      dictionary={element: num for element in letter}
      for element, value in dictionary.items():
        if element in new_dictionary:
          new_dictionary[element]+=value
        else:
          new_dictionary[element]=value
    ordered_dict_items = sorted(new_dictionary.items())
    ordered_dict = {}
    for item in ordered_dict_items:
      ordered_dict[item[0]] = item[1]
    ordered_dict = dict(ordered_dict)

    


    return (ordered_dict)

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data=open("data.csv","r").readlines()
    dictionary={}
    new_dictionary={}
    for line in data:
      line=line.strip().split('\t')
      key=line[0]
      tuplas=line[4].split(",")
      num_list=[]
      for element in tuplas:
        num_list.append(int(element.split(":")[1]))
      if key in new_dictionary:
          dictionary[key].extend(num_list)
      else:
          dictionary[key]= num_list
      for key, num_list in dictionary.items():
        new_dictionary[key] = sum(num_list)
    ordered_dict_items = sorted(new_dictionary.items())
    ordered_dict = {}
    for item in ordered_dict_items:
      ordered_dict[item[0]] = item[1]
    ordered_dict = dict(ordered_dict)
    
    return (ordered_dict)
    

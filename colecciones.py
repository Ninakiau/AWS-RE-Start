"""
Lista una colección ordenada de elementos 
Cualquier tipo de dato puede ser un elemento
Son mutables, pueden cambiar en cualquier momento del código
Acepta elementos repetidos

"""

myFruitList = ["pera", "banana", "mango"]
print(myFruitList)
print(type(myFruitList))

# Acceder a un elemento por posición

# Muestra el primer elemento
print(myFruitList[0])

# Muestra el segundo elemento de la lista
print(myFruitList[1])

# Muestra el tercer elemento de la lista
print(myFruitList[2])

# Cambio mango por melón
myFruitList[2]="melon"
print(myFruitList)

# Métodos de las listas 

# .append() agregar un elemento a la lista
# añadir tomate
myFruitList.append("tomate")
myFruitList.append("tomate")
print(myFruitList)

# .remove remueve el primer elemento tomate encontrado
myFruitList.remove("tomate")
print(myFruitList)

"""
Tupla
Acepta repetidos
Es inmutable
Se define con ()
"""

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Accedemos a apple
print(myFinalAnswerTuple[0])

# Accedemos a banana 
print(myFinalAnswerTuple[1])

# Accedemos a pineapple
print(myFinalAnswerTuple[2])

"""
Diccionario 
Es una colección ordenada (desde la versión 2.7) de  elementos clave valor
SOn mutables
clave: entero o string
valor: cualquier tipo de dato

"""

fondosRestart = {
    "Mario": "Amarillo",
    "Luna": "Naranja",
    "Jorge": "Negro",
    "Matias": "Blanco",
    "Laura": "Negro"
}

print(fondosRestart)
print(type(fondosRestart))

# Traer fondo de Jorge 
print(fondosRestart["Jorge"])

# Agregar un elemento sólo creando la clave

fondosRestart["Gustavo"]= "gris"
print(fondosRestart)
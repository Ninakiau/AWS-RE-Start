"""
Ciclo while

Es una sentencia que repetirá un conjunto de instrtucciones mientras que 
una condición sea verdadera

Loop infinito

"""

contador = 1

while contador <10:
    print(contador)
    contador+=1
    
    
estudiantes = []
# opcion = input("Quiere continuar? Si o No")
# while opcion != "No":
#     # De forma provicional guardamos el estudiante en una variable
#     nombre= input("Ingresa un estudiante: ")
    
#     ## Llamo a la lista para agregarlo
#     estudiantes.append(nombre)
#     opcion = input("Quiere continuar? Si o No")
    
# print(estudiantes)

while True:
    nombre = input("Ingresa un estudiante: ")
    estudiantes.append(nombre)
    
    opción = input("Quiere continuar? Si o No ")
    
    if opción == "No":
        break
    
print(estudiantes)

for x in estudiantes:
    print(f"Hola {x}")
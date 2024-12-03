"""
Ciclo for
Sé exactamente cuando voy a parar el ciclo
es ideal para recorrer listas, tuplas, diccionarios, etc (secuencias)

Puedo nombrar una variable:
* No use caracteres especiales
* No empiece por un número
* No contenga espacios


* Si puede tener un número en el medio o al final 
* Puede tener _
* Puede tener mayúsculas y minúsculas

"""

lista = ["Dinosaurio", 23, True, 45.5, "Amazon"]

for x in lista: 
    print (f"Elemento {x}")
    


# Dada la siguiente lista imprime SOLO los números pares
numeros = [2, 45, 19, 13, 178]

print("N  u  m  e  r  o  s    p  a  r  e  s")
for x in numeros:
    if x%2 == 0:
        print(x)

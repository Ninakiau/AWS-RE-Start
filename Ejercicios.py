# Ejercicio 1: Suma de números del 1 al 10

# suma = 0
# for x in range(1, 11):
#     suma +=x
#     print(suma)
    


# print(f"La suma es: {suma}")


# Ejercicio 2: Tablas de multiplicar Escribe un programa que imprima la tabla 
# de multiplicar del 5 (del 1 al 10).

# for i in range(1, 11):
#     print(f"5 x {i} = {5*i}")


# print("OTRA TABLA DE MULTIPLICACIón")
# cont=1
# while cont <=10:
#     print(f"5 x {cont} = {5*cont}")
#     cont+=1

# Ejercicio 3: Contar vocales en una palabra
# Pide al usuario una palabra y cuenta cuántas vocales tiene.

# vocales=["a", "e", "i", "o", "u"]
# palabra= input("Ingrese una palabra: ")
# contador=0

# # for x in palabra:
# #     if x in vocales:
# #         contador+=1
        
# # print(contador)

# contadorA=0
# contadorE=0
# contadorI=0
# contadorO=0
# contadorU=0

# for x in palabra:
#     if x == "a":
#         contadorA+=1
#     if x =="e":
#         contadorE+=1
#     if x =="i":
#         contadorI+=1
#     if x =="o":
#         contadorO+=1
#     if x =="u":
#         contadorU+=1
        
# print(contadorA)
# print(contadorE)
# print(contadorI)
# print(contadorO)
# print(contadorU)

# Pedimos al usuario que ingrese una palabra
# palabra = input("Ingresa una palabra: ").lower()
 
# # Definimos las vocales y un diccionario para contar
# vocales = "aeiou"
# contador_vocales = {vocal: 0 for vocal in vocales}
# print(vocales)
# print(contador_vocales)
# # Recorremos cada letra de la palabra
# for letra in palabra:
#     if letra in vocales:
#         print(letra)
#         contador_vocales[letra] += 1
 
# # Mostramos el resultado
# print(contador_vocales.items())
# for vocal, cantidad in contador_vocales.items():
#     print(f"La vocal '{vocal}' aparece {cantidad} veces.")


# # Ejercicio 4: Encontrar el número mayor
# # Dado un listado de números, encuentra el mayor usando un ciclo y un condicional.
# numeros= [2,564,65,77,3,543,32,12,4,33,52,65,65,74]
# mayor=0
# while 
# for x in numeros
#     mayor


# Ejercicio 5: Contar hasta que el usuario lo detenga
# Usa un ciclo while para imprimir números empezando desde 1, hasta que el usuario escriba stop.

# numero = 1
 
# while True:

#     print(numero)

#     numero += 1

#     opcion = input("para seguir presione enter, para detener escriba stop ")

#     if opcion == "stop":
#         break


# Ejercicio 7: Número par o impar
# Pide al usuario un número y determina si es par o impar.Hay que hace un lista números y determinar cuantos pares e impares hay
lista = []
pares=0
impares=0

while True:
    num = int(input("Ingrese un numero: "))
    lista.append(num)
    respuesta = input("Quieres seguir agregando números: True para si y False para no: " )
    if respuesta == "False":
        print("adios")
        break
        


for num in lista: 
    if num%2 == 0:
        pares+=1
       
    else:
        impares+=1
        
        
print(f"Hay {pares} números pares y {impares} números impares")
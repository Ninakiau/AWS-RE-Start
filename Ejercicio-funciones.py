
"""
Crea un programa para saludar a los bellos estudiantes del curso
"""

"""
Función

Es un conjunto de instrucciones que se agrupan para reutilizarse en el código


Cuando note que se repite muchas veces la misma instrucción
probablemente necesite una función

"""

# def nombreFuncion (arg1, arg2):

# def saludar():
#     print("Hola")

# # Argumentos
# def saludarEstudiante(nombre):
#     print(f"Hola {nombre}")

# # Llamado de la función
# saludarEstudiante("Hernan")

# # Retornando un valor
# def calcularEdad(anio):
#     edad = 2024 - anio
#     return edad
    

# # Llamado de la función
# entrada = int(input("Ingresa el año de nacimiento: "))

# resultado = calcularEdad(entrada)



"""
Genera una función que permita calcular el precio final de un producto

El usuario ingresa el producto y tú retornarás el valor + el IVA (19%) = 0.19


Ejemplo: 
Entrada: 1000
Salida: 1190
"""
precio = int(input("Ingrese el valor del producto: "))

def calcularIVA(precio):
    return precio*1.19
    
    
print(calcularIVA(precio))
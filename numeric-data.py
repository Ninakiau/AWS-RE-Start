# Orden de operaciones
"""
Comentario de varias líneas

"""

print("Python has three numeric types: int, float, and complex")
valor =5
print(valor)
print(type(valor))
print(f"Hola el valor es {valor} y el tipo de dato es {type(valor)}") 

# float: decimal -1.56565

valor= 4.55555
print(f"el valor {valor} y el tipo es {type(valor)}")

#complex: 4j 25j 4.5j
valor = 4j
print(f"el valor {valor} y el tipo es {type(valor)}")

valor= True
print(f"el valor a {valor} y el tipo es {type(valor)}")

"""
float()
complex()
bool()
str()
"""

a = 45
b= float(a)
print(f"A es de tipo {type(a)}, b es de tipo {type(b)}")
a = "hola mundo"
b= float(a)
print(f"A es de tipo {type(a)}, b es de tipo {type(b)}")
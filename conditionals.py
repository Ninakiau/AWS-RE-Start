"""
Condicionales

Van a realizar una acción en función de una evaluación 

Operadores de verdad
> mayor
< menor
>= mayor igual
<= menor igual
== igual
!= diferente


Operadores lógicos
AND 
OR 
NOT
"""

edad = 18
nombre = "Claudia"
# if [evaluación que dará true or false]

if edad >= 18:
    if nombre != "Claudia":
        print("Bienvenida");
        print("hello")


if edad >= 18 or nombre != "Patricio":
    print("Yay");


if edad >= 18 and nombre != "Patricio":
    print("Yayyy");
    
edad = 180

if edad != 18:
    print("Fuera");

"""
Sólo con condicionales
"""
pais = input("Ingresa tu país ").lower()

if pais == "chile":
    print("Wena po")
elif pais == "colombia":
    print("Hola parce")
elif pais == "venezuela":
    print("Hola chamo")
elif pasi == "argentina":
    print("Hola che querido")
else
    print("sayonara, good bye")



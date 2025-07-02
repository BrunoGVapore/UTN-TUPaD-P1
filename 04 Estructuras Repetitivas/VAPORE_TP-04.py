# Práctico 4: Estructuras repetitivas

# Actividad 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for num in range(101):
    print(num)

# Actividad 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
from math import trunc

contador = 0
num = int(input("Ingrese un número entero: "))

if num >= 10 or num <= -10:
    while num >= 1 or num <= -1:
        num = trunc(num) / 10
        contador += 1
else:
    contador = 1

print(f"La cantidad de dígitos del número ingresado es {contador}")

# Actividad 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingr#ese el segundo número: "))
suma = 0

if num1 <= num2:
    for cont in range(num1+1, num2):
        suma += cont
else:
    for cont in range(num1-1, num2, -1):
        suma += cont
print(f"La suma de todos los números enteros entre los dos números ingresados es {suma}")

# Actividad 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
num = 1
suma = 0
while num != 0:
    num = int(input("Ingrese un número: "))
    suma += num
print(f"La suma total es {suma}")

# Actividad 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
from random import randint
numAzar = randint(0,9)
numUsuario = -1
contador = 0

while numAzar != numUsuario:
    numUsuario = int(input("Ingrese un número entre el 0 y el 9 e intente adivinar: "))
    if numUsuario < 0 or numUsuario > 9:
        print("ERROR. Ingrese otro número")
    else:
        print("Falló")
        contador += 1
print(f"Felicidades. La cantidad de intentos fue {contador}. El número era {numAzar}")

# Actividad 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for num in range(100,-1,-2):
    print(num)

#Actividad 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
suma = 0
num = int(input("Ingrese un número entero positivo para calcular la suma de todos los números desde el 0: "))
if num > 0:
    for cont in range(num+1):
        suma += cont
else:
    print("Debe ingresar un número entero positivo. No se sumó ningún número.")
print(f"La suma desde el 0 hasta {num} es: {suma}")

#Actividad 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos.
contPar = 0
contImpar = 0
contPositivo = 0
contNegativo = 0

for x in range (100):
    num = int(input("Ingrese un número entero: "))
    if num != 0:
        if num > 0:
            contPositivo += 1
        else:
            contNegativo += 1
        if num % 2 == 0:
            contPar += 1
        else:
            contImpar += 1
    else:
        print("Usted ingresó 0, no sumará ningún contador.")

print(f"{contPar} números son pares; {contImpar} números son impares; {contPositivo} números son positivos; y {contNegativo} números son negativos")

# Actividad 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
suma = 0
for x in range (100):
    num = int(input("Ingrese un número entero: "))
    suma += num
print(f"La media es {suma/100}")

# Actividad 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
num = int(input("Ingrese un número: "))
numCadena = str(num)
longitud = len(numCadena)
invertido = ""

while longitud > 0:
    invertido += numCadena[longitud - 1]
    longitud -= 1
if num < 0:
    invertido = "-" + invertido[longitud:-1]
print(f"El número invertido es {invertido}")
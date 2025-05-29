# Librerias utilizadas
import math
from statistics import mean

# Listado de funciones

def imprimir_hola_mundo():   # Imprime por pantalla el mensaje "Hola Mundo!"
    print("Hola Mundo!")

def saludar_usuario(nombre): # Saludo personalizado según parámetro ingresado por el usuario.
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):                     # Imprime la información personal según parámetros ingresados por el usuario.
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):  # Calcula el área del circulo según el valor de radio ingresado.
    area = math.pi * (radio ** 2)  # Se utiliza pi desde la libreria importada math para tener un valor más exacto
    return round(area, 2)          # Con la función round(parámetro, 2) al valor obtenido lo corto y me quedo con 2 numeros decimales.

def calcular_perimetro_circulo(radio): # Calcula el perímetro del circulo según el valor de radio ingresado.
    perimetro = (2 * math.pi * radio)  # Se utiliza pi desde la libreria importada math para tener un valor más exacto
    return round(perimetro, 2)         # Con la función round(parámetro, 2) al valor obtenido lo corto y me quedo con 2 numeros decimales.

def segundos_a_horas(segundos):     # Calcula la cantidad de horas segundo la cantidad de segundos ingresados.
    horas = float(segundos / 3600)  # Explicación del cálculo: 1 hora son 60 minutos y 1 minuto son 60 segundos: 60 * 60 = 3600 segundos
    return round(horas, 2)          # Con la función round(parámetro, 2) al valor obtenido lo corto y me quedo con 2 numeros decimales.

def tabla_multiplicar(numero):                    # Genera por pantalla la tabla de multiplicar del número ingresado, desde el 1 al 10.
    for i in range(1, 11):                        # El bucle comienza en 1 y termina en 10 en virtud de los parámetros de range.
        print(f"{numero} x {i} = {(numero * i)}") # Imprime por pantalla el numero ingresado; el valor de i desde el 1 al 10; y el resultado de la multiplicación.

def operaciones_basicas(a, b):                                                  # Función de operaciones básicas con resultados en una tupla
    while b == 0:                                                               # Se mantiene en el bucle hasta que b sea distinto de 0 (b no puede ser 0 par ala división)
        b = int(input("ERROR. Ingrese el segundo número distinto de cero: "))   # Seguirá preguntando un nuevo número hasta que no se ingrese el 0
    return ((a + b), (a - b), (a * b), (a / b))                                 # Devuelve una tupla con los resultados

def calcular_imc(peso, altura):     # Calcula el IMC en base al peso en kilogramos y la altura en metros
    return peso / (altura ** 2)

def celsius_a_fahrenheit(celsius):  # Pasaje de grados Celsius a grados Fahrenheit
    return 9/5 * celsius + 32

def calcular_promedio(a, b, c):       # Calcula el promedio de tres valores
    promedio = float(mean([a, b, c])) # Se llama a función mean con () y se crea una lista [] con los valores para hacer el cálculo
    return promedio
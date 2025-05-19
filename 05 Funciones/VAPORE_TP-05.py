# Práctico 5: Funciones
import myFunctions

# Actividad 1: 
# Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

myFunctions.imprimir_hola_mundo()

# Actividad 2:
# Crear una función llamada saludar_usuario(nombre) que reciba  como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

nombre = input("Ingrese su nombre: ")
myFunctions.saludar_usuario(nombre)

# Actividad 3: 
# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
# que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
myFunctions.informacion_personal(nombre, apellido, edad, residencia)

# Actividad 4: 
# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

radio = float(input("Ingrese el radio del círculo: "))
print(f" El área del círculo es {myFunctions.calcular_area_circulo(radio)} y su perímetro es {myFunctions.calcular_perimetro_circulo(radio)}")

# Actividad 5: 
# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos equivale a {myFunctions.segundos_a_horas(segundos)} hora/s")

# Actividad 6: 
# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

numero = int(input("Ingrese un número: "))
myFunctions.tabla_multiplicar(numero)

# Actividad 7: 
# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número distinto de cero: "))
resultado = myFunctions.operaciones_basicas(num1, num2)
print(f"La suma es {resultado[0]} \nLa resta es {resultado[1]} \nLa multiplicación es {resultado[2]} \nLa división es {resultado[3]}")

# Actividad 8:
# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

peso = float(input("Ingrese su peso es kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"El IMC es {round(myFunctions.calcular_imc(peso, altura), 2)}")

# Actividad 9: 
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

celsius = float(input("Ingrese los grados Celcius: "))
print(f"{celsius} grados Celcius equivale a {myFunctions.celsius_a_fahrenheit(celsius)} grados Fahrenheit")

# Actividad 10: 
# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
print(f" El promedio de los numeros ingresados es {myFunctions.calcular_promedio(num1, num2, num3)}")
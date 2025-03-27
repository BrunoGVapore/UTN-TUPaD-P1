# Práctico 1: Estructuras secuenciales

# Actividad 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# Actividad 2: Crear un programa que pida al usuario su nombre # e imprima por pantalla un saludo usando el nombre ingresado. 
nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}!")

# Actividad 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
lugar = input("Ingrese su lugar de residencia:")
print(f"Hola {nombre} {apellido}, así que tienes {edad} años y eres de {lugar}")

# Actividad 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = float(input("Ingrese el radio del círculo en cm:"))
area = 3.14 * (radio ** 2)
perimetro = (2 * 3.14 * radio)
print(f"El área del circulo es {area} cm2 y su perímetro es {perimetro} cm aproximadamente")

# Actividad 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese los segundos:"))
horas = segundos / (60 * 60)
print(f"{segundos} segundos equivale a {horas} horas")

# Actividad 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
num = int(input("Ingrese un número para generar la tabla de multiplicar: "))
print(f"{num} x 0 es = ", num*0)
print(f"{num} x 1 es = ", num*1)
print(f"{num} x 2 es = ", num*2)
print(f"{num} x 3 es = ", num*3)
print(f"{num} x 4 es = ", num*4)
print(f"{num} x 5 es = ", num*5)
print(f"{num} x 6 es = ", num*6)
print(f"{num} x 7 es = ", num*7)
print(f"{num} x 8 es = ", num*8)
print(f"{num} x 9 es = ", num*9)
print(f"{num} x 10 es = ", num*10)

# Actividad 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número distinto de 0: "))
print(f"{num1} + {num2} = ", num1 + num2)
print(f"{num1} / {num2} = ", num1 / num2)
print(f"{num1} x {num2} = ", num1 * num2)
print(f"{num1} - {num2} = ", num1 - num2)

# Actividad 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso es kilogramos: "))
print("Su IMC es ", peso / (altura ** 2))

# Actividad 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
grados = float(input("Ingrese los grados Celcius"))
print(f"{grados} grados Celcius equivale a", 9/5 * grados + 32)

# Actividad 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números es {promedio}")
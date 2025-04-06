# Práctico 3: Estructuras condicionales

# Actividad 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
MAYORIA_EDAD = 18
edad = int(input("Ingrese su edad: "))
if edad >= MAYORIA_EDAD:
    print("Es mayor de edad")

# Actividad 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
NOTA_MINIMA = 6
nota = int(input("Ingrese la nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Actividad 3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Actividad 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Ud. es Niño/a")
elif edad >= 12 and edad < 18:
    print("Ud. es Adolescente")
elif edad >= 18 and edad < 30:
    print("Ud. es Adulto/a Joven")
else:
    print("Ud. es Adulto")

# Actividad 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
password = len(input("Ingrese una contraseña: "))
if password >= 8 and password <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Actividad 6: ...escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = float(mode(numeros_aleatorios))
mediana = float(median(numeros_aleatorios))
media = float(mean(numeros_aleatorios))

if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana and mediana == moda:
    print("No hay sesgo")
else:
    pass

# Actividad 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase = input("Ingrese una frase o palabra: ")
if frase[-1] == "a" or frase[-1] == "e" or frase[-1] == "i" or frase[-1] == "o" or frase[-1] == "u":
    print(f"{frase}!")
else:
    print(frase)

# Actividad 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese la opción 1 para su nombre en Mayúsculas; opción 2 para minusculas; y opción 3 solo primera letra en Mayúscula: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    pass

# Actividad 9:  Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: ● Menor que 3: "Muy leve" (imperceptible). ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible). ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos). ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("\"Muy leve\" (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("\"Leve\" (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("\"Moderado\" (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("\"Fuerte\" (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("\"Muy Fuerte\" (puede causar daños significativos)")
else:
    print("\"Extremo\" (puede causar graves daños a gran escala)")

# Actividad 10: Utilizando la información aportada en la siguiente tabla sobre las estaciones del año ... Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("¿En qué hemisferio se encuentra? (N para Norte/S para Sur): ").upper()
mes = input("Qué mes del año es?: ").lower()
dia = int(input("Qué día es?: "))

if hemisferio == "N":
    if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
        print("Ud. se encuentra en Invierno")
    elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
        print("Ud. se encuentra en Primavera")
    elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
        print("Ud. se encuentra en Verano")
    else:
        print("Ud. se encuentra en Otoño")
else:
    if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
        print("Ud. se encuentra en Verano")
    elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
        print("Ud. se encuentra en Otoño")
    elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
        print("Ud. se encuentra en Invierno")
    else:
        print("Ud. se encuentra en Primavera")
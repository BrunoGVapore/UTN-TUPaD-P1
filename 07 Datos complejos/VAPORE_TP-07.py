# Práctico 7: Estructuras de datos complejas 

# Actividad 1: Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

# Actividad 2: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#  Banana = 1330
#  Manzana = 1700
#  Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# Actividad 3: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# Actividad 4: Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

numeros_telefonicos = {}
for i in range(5):
    print(f"Vamos a cargar el contacto N°{i+1}")
    nombre = input("Ingresar nombre: ")
    telefono = input("Ingresar número de teléfono: ")
    numeros_telefonicos[nombre] = telefono

consulta = input("Buscar en la agenda de contactos telefónicos por nombre: ")
if consulta in numeros_telefonicos:
    print(f"El teléfono de {consulta} es {numeros_telefonicos[consulta]}")
else:
    print("El nombre ingresado no se encuentra en la agenda.")

# Actividad 5: Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresar una frase: ")
lista_palabras = frase.split()

palabras_unicas = set(lista_palabras)
print(palabras_unicas)

contador_palabras = {}
for i in lista_palabras:
    contador_palabras[i] = contador_palabras.get(i, 0) + 1
print(contador_palabras)

# Actividad 6: Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresa el nombre del alumno N°{i+1}: ")
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Ingresar nota N°{j+1} de {nombre}: "))
                if nota >= 1 and nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota fuera de rango")
            except ValueError:
                print("Error")
    alumnos[nombre] = tuple(notas)

print(alumnos)

for nombre, notas in alumnos.items():
    suma = sum(notas)
    promedio = sum(notas) / 3
    print(f"El promedio de {nombre} es {promedio:.2f}")


# Actividad 7: Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

estudiantes_aprobados_parcial_1 = {1, 2, 3, 4, 5, 7, 9, 10}
estudiantes_aprobados_parcial_2 = {2, 4, 5, 6, 8, 9}

ambos_aprobados = estudiantes_aprobados_parcial_1 & estudiantes_aprobados_parcial_2
print(ambos_aprobados)

solo_uno_aprobado = estudiantes_aprobados_parcial_1 ^ estudiantes_aprobados_parcial_2
print(solo_uno_aprobado)

al_menos_uno_aprobado = estudiantes_aprobados_parcial_1 | estudiantes_aprobados_parcial_2
print(al_menos_uno_aprobado)


# Actividad 8: Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

golosinas = {
    "Chocolate": 25,
    "Caramelos": 10,
    "Gomitas": 5,
}

consulta = input("Ingresa un producto para consultar o agregar: ")
if consulta in golosinas:
    stock = int(input(f"Hay stock de {consulta} por {golosinas[consulta]} unidades. ¿Cuánto más desea agregar?"))
    golosinas[consulta] += stock
else:
    golosinas[consulta] = consulta
    stock = int(input(f"Se agregó el producto {consulta}. ¿Cuántas únidades se agregan?"))
    golosinas[consulta] = stock

print(golosinas)

# Actividad 9: Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "10:30 hs."): "Entrevista",
    ("martes", "9:00 hs."): "Congreso",
    ("jueves", "16:00 hs."): "Reunión",
    ("viernes", "09:00 hs."): "Examen"
}

consulta = input("Ingrese el día de la semana para consultar su agenda: ").lower()
for (dia, hora), evento in agenda.items():
    if consulta == dia:
        print(f"A las {hora}: {evento}")


# Actividad 10: Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

mundo = {
    "Argentina": "Buenos Aires",
    "Japón": "Tokio",
    "Italia": "Roma",
    "Irlanda": "Dublín"
}

mundo_invertido = {}
for pais, capital in mundo.items():
    mundo_invertido[capital] = pais

print(f"Ahora las keys son las capitales y los values los países:\n{mundo_invertido}")
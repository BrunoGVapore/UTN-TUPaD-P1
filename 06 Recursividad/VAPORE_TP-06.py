# Práctico 6: Aplicación de la Recursividad

# 1) Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial 
# de todos los números enteros entre 1 y el número que indique el usuario.

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

num = int(input("Ingrese un numero para calcular el factorial: "))
print(factorial(num))

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci 
# en la posición indicada. Posteriormente, muestra la serie completa hasta 
# la posición que el usuario especifique.

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2) # Hace dos llamados a la función
    
pos = int(input("Ingrese la posición de Fibonacci: "))
print(f"En la posición {pos}, el valor de Fibonacci es {fibonacci(pos)}") 

serie = []
for i in range(pos+1):  # iteración para agregar en una lista la serie de fibonacci hasta la posición elegida (+1 porque la lista arranca a contar desde 0).
    serie.append(fibonacci(i))
print(f"La serie es {serie}")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula n^𝑚= 𝑛∗𝑛^(𝑚−1). Prueba esta función en un algoritmo general.

# ----Función----
def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base 
    elif exponente >= 2:
        return base * potencia(base, exponente - 1)             # Para exponentes positivos mayores a 1
    else:
        return float(1 / base * potencia(base, exponente + 1))  # Para exponentes negativos, devuelve número flotante

# ----Algoritmo General----

print("Para calcular la potencia de un número elevado a un exponente, deberá ingresar los siguientes valores: ")
base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))

if exp == 0:
    print("Cualquier número elevado a 0, da como resultado 1")
elif exp == 1:
    print("Cualquier número elevado a 1, da como resultado la base")
elif exp >= 2:
    print(f"Se utiliza la siguiente fórmula para números positivos: n^𝑚 = n * n^(𝑚 - 1)")
    print(f"Con los datos ingresados quedaría: {base} * {base}^({exp}-1)")
else:
    print(f"Se utiliza la siguiente fórmula para números negativos: n^-𝑚 = 1/n^m = 1 / n*n^(-𝑚 - 1)")
    print(f"Con los datos ingresados quedaría: 1 / ({base} * {base}^(-({exp})-1))") 

print(f"El resultado de {base}^{exp} es: {potencia(base, exp)}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.

def dec_a_bin(decimal):
    if decimal <= 0:
        return "ERROR! Esta función solo permite números enteros positivos"
    elif decimal == 1:
        return "1"
    else:
        return dec_a_bin(decimal // 2) + str(decimal % 2)  # La función se llama a sí misma para el cociente y se agrega el residuo a la cadena de texto.

num = int(input("Ingrese un número entero positivo en base decimal: "))
print(dec_a_bin(num))


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes,
#  y devuelva True si es un palíndromo o False si no lo es.
# Requisitos: La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:         # Si la longitud llega a 1 es palíndromo. El <= permite que la longitud sea par, porque en este caso la cadena queda vacía.
        return True
    elif palabra[0] != palabra[-1]: # Compara los extremos y devuelve falso si son distintos, descartanto que la palabra sea palíndromo.
        return False
    else: 
        return es_palindromo(palabra[1:-1]) # La función se llama a sí misma sin tener en cuenta la primer y última letra, armando una nueva cadena.

palabra = input("Ingresa una palabra para saber si es palíndromo: ")
if " " in palabra or "á" in palabra or "é" in palabra or "í" in palabra or "ó" in palabra or "ú" in palabra:
    print("ERROR! No puede ingresar espacios ni tildes")
else:
    print(es_palindromo(palabra))


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones: No se puede convertir el número a string. Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):
    if n <= 0:
        return "ERROR! Esta función solo permite números enteros positivos"
    elif n < 10:          # Caso Base: menor a 10 para que el último valor se sume como dígito
        return n
    else:
        return suma_digitos(n // 10) + (n % 10)  # La función se llama a sí misma para obtener el nuevo número al realizar la división entera del anterior. Al tiempo que calcula en cada llamado el resto de la división, que se va a ir sumando para el resultado final.

num = int(input("Ingrese un número entero positivo para calcular la suma de los dígitos: "))
print(suma_digitos(num))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
# en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    if n <= 0:
        return "ERROR! Esta función solo permite números enteros positivos"
    elif n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

bloques = int(input("Ingrese el número de bloques en el nivel inferior para calcular los bloques totales de su pirámide: "))
print(contar_bloques(bloques))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) 
# que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
# y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero <= 0:
        return "ERROR! Esta función solo permite números enteros positivos"
    else:
        return (1 if digito == numero % 10 else 0) + contar_digito(numero // 10, digito)

num = int(input("Escribí el número: "))
dig = int(input("Escribí el dígito a contar: "))

print(contar_digito(num, dig))
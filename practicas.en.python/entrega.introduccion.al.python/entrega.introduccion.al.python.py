# Ingresar números enteros hasta cargar un arreglo con los primeros 10 números impares múltiplos de 3 o hasta que se ingrese un cero. Mostrarlo y calcular:
#
#   Mostrar cuantas veces se repite el valor mínimo y que posiciones ocupan. Si no hubiese repeticiones mostrar una leyenda. (No se puede ordenar el arreglo original, n i usar la funcion min del lenguaje para resolver este punto)
#   Generar otro arreglo con los valores que se encuentran en el arreglo original que están entre el promedio de los números ingresados y el mínimo. Si no los hay, mostrar una leyenda. (No se puede ordenar el arreglo original)
#   Ingresar un numero por teclado y cambiar todos sus apariciones por su opuesto. Si no se realizaron cambios mostrar un mensaje indicándolo (Este punto se debe realizar sobre el mismo arreglo, no se puede generar otro).
#
# Nota: La carga inicial se debe hacer en un único arreglo. No se pueden utilizar arreglos auxiliares para resolver los puntos planteados a excepción que se lo solicite.
#
# Los criterios de evaluación que se tendrán en cuenta serán:
#
#   Que el programa no contenga errores de sintaxis y que se pueda ejecutar.
#   Que el programa realice lo que se pide.
#   Utilización correcta de los ciclos repetitivos y estructuras condicionales.
#   Utilización correcta de los símbolos de comparación, lógicos y matemáticos.
#   Manejo de máximos y mínimos, contadores, acumuladores, promedios, porcentajes.
#   Buen uso de la lógica de programación (que sea eficiente).
#   Que el programa no corte abruptamente y que no utilice banderas, ni variables globales.
#   Que el programa este modularizado, y se haga reutilización de código en caso de ser necesario.
#   Manejo de arreglos y utilización de  funciones propias del programador.
#   Que no se utilicen sentencias break o sentencias return dentro de ciclos.
#   Validación de los datos de entrada en caso de ser necesario
#   Fecha limite de entrega 22/03/2021 inclusive. Adjuntar solo el archivo .py con la resolución. La resolución del ejercicio es individual, NO GRUPAL.
 

def EsMultiploDe(a, b):
    return a % b == 0

def EsPar(a):
    return EsMultiploDe(a, 2)

def MostrarError(mensaje):
    print("¡Error: " + mensaje + "!")

def IngresarNumeroEntero():
    x = 0
    error = True
    while error:
        try:
            x = int(input("Ingesar número: "))
            error = False
        except:
            MostrarError("El valor ingresado no es un número entero")
    return x

def HayElementos(numbers):
    return len(numbers) > 0

def MostrarArreglo(numbers):
    if HayElementos(numbers):
        for i in numbers:
            print(i)

def Minimo(numbers):
    result = 0
    if HayElementos(numbers):
        result = numbers[0]
        for i in range(1, len(numbers)):
            if(numbers[i] < result):
                result = numbers[i]
    return result

def MostrarMinimos(numbers, min):
    if HayElementos(numbers):
        print("Valor mínimo: " + str(min))
        for i in range(len(numbers)):
            if numbers[i] == min:
                print("Posición: " + str(i))
    else:
        print("El arreglo está vacío")

def Promedio(numbers):
    ce = 0
    result = 0
    for i in numbers:
        result = result + i
        ce = ce + 1
    if ce > 0:
        result = result / ce

    return result

def MostrarMinimoPromedio(numbers, min):
    found = False
    if HayElementos(numbers):
        p = Promedio(numbers)
        print("Promedio: " + str(p))
        for i in numbers:
            if i > min and i < p:
                print("Entre el mínimo y el promedio: " + str(i))
                found = True
    if not(found):
        print("No hay números entre el mínimo y el promedio")

def CambiarPorOpuesto(numbers):
    if HayElementos(numbers):
        print("Cambiar por opuesto: ")
        n = IngresarNumeroEntero()
        for i in range(len(numbers)):
            if numbers[i] == n:
                numbers[i] = -numbers[i]
    MostrarArreglo(numbers)

numbers = []

x = IngresarNumeroEntero()
while x != 0 and len(numbers) < 10:
    if not(EsPar(x)) and EsMultiploDe(x, 3):
        numbers.append(x)
    x = IngresarNumeroEntero()

MostrarArreglo(numbers)
m = Minimo(numbers)
MostrarMinimos(numbers, m)
MostrarMinimoPromedio(numbers, m)
CambiarPorOpuesto(numbers)
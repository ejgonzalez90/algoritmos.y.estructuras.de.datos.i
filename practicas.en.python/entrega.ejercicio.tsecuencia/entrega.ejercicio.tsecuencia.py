# Dada una secuencia que contiene palabras separadas por uno o más blancos, donde cada palabra está formada por los caracteres ‘0’, ‘1’, ‘2’, ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’, ‘9’  (lo que significa que cada palabra es la representación decimal de un entero). Se pide crear una nueva secuencia con los numeros capicuas que hay en la secuencia original, separados por comas

# Ejemplo : 123     17  373   167  71 28 125   313 317     1331     337  1250 5  25 409

# SS: 373, 313, 1331, 5

# NOTA: 

# Se desconoce la longitud de la secuencia y de las  palabras que la conforman.
# No se pueden usar listas de python, ni arreglos,  ni strings. 
# La secuencia se debe leer y tratar, no cargar en una estructura adicional.
# Cada palabra debe ser tratada como un número
# La solución debe esta modulada.
# Para resolver el ejercicio deben utilizar el modulo de secuencias de la cátedra.
# La carga de la secuencia debe estar en un programa separado,  no forma parte del programa de aplicación.
# Fecha limite de entrega 12/04/2021. Se debe entregar la resolución del problema en Python. Adjuntar solo el archivo .py con la resolución.

import imp
TSecuencia = imp.load_compiled("TSec", "../lib/TSecuencia.cpython-37.pyc")
TDato = imp.load_compiled("TDato", "../lib/TDato.cpython-37.pyc")

separador = " "
finSecuencia = "*"

e = TSecuencia.TSecuenciaE()
datoC = TDato.TdatoC()

def MostrarError(mensaje):
    print("¡Error: " + mensaje + "!")

def LeerNumeroEntero(e, datoC, esPrim):
    error = True
    try:
        if esPrim:
            TSecuencia.SleerprimE(e, datoC)
        else:
            TSecuencia.SleersigE(e, datoC)            
        if datoC.valor != separador and datoC.valor != finSecuencia:
            datoC.valor = int(datoC.valor)
        error = False
    except:
        MostrarError("El valor leído no es un número entero")
    return error

def EsInicio(ant, c):
    return ant == separador and c != separador

def EsMedio(ant, c):
    return ant != separador and c != separador

def EsFin(ant, c):
    return ant != separador and (c == separador or c == finSecuencia)

def TratarInicio(valor):
    return valor

def TratarMedio(valor, numero):
    return numero * 10 + valor

# La carga de la secuencia debe estar en un programa separado,  no forma parte del programa de aplicación.
#   --> No me queda claro si "carga" es la lectura o la escritura de la secuencia
#       En el ejemplo se usa "carga" para escritura, asi que asumo que solo se trata de mostrar el dato
def TratarFin(numero, resultado):
    if EsCapicua(numero):
        if resultado != "":
            resultado += ", "
        resultado += str(numero)
    return resultado

def EsCapicua(valor):
    es = False
    i = 0
    aux1 = 0
    aux2 = valor
    while aux2 > 0:
        aux1 = aux1 * 10 + aux2 % 10
        aux2 = aux2 // 10
        i += 1
    if valor == aux1:
        es = True
    return es

ant = separador
numero = 0
error = LeerNumeroEntero(e, datoC, True)
resultado = ""
while (not error and not TSecuencia.SfinE(e)):
    if EsInicio(ant, datoC.valor):
        numero = TratarInicio(datoC.valor)
    else:
        if EsMedio(ant, datoC.valor):
            numero = TratarMedio(datoC.valor, numero)
        elif EsFin(ant, datoC.valor):
                # Para determinar si el numero es capicúa, estoy olbigado a leerlo por completo
                # si el número fuese 1221 (Capicúa), y estoy en el medio (12) el valor EsCapicua(numero) retornaría falso
                # por otro lado, si la "carga" se refiere a la escritura de la secuencia, podría evitarse la concatenación de str, escribiendo directamente
                # en esta.
                resultado = TratarFin(numero, resultado)
    ant = datoC.valor
    error = LeerNumeroEntero(e, datoC, False)

print("SS: " + resultado)

# carga de una secuencia
# --> Ignorar si "carga" se refiere a la escritura de la secuencia, ya que se pidió ignorar la misma
s = TSecuencia.TSecuenciaS()

TSecuencia.SprepararS(s)
for letra in resultado:
    datoC.valor = letra
    TSecuencia.SescribirS(s, datoC)
TSecuencia.SmarcarS(s)

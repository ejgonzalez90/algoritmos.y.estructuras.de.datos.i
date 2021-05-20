# Ingresar palabras desde teclado dentro de una cola. La carga finaliza al leer la palabra "FIN". 
# Se desea mostrar las palabras ingresadas que se encuentran en la cola ordenadas de la mas larga a la mas chica en longitud pero invertida
# Entrada:  Hola como me esta yendo en algoritmos. No creo que estemos bien FIN
# Salida: somtirogla sometse odney aloH omoc atse oerc neib euq em ne oN

# NOTA:
# La solución debe esta modularizada.
# Para resolver el ejercicio deben utilizar el modulo de TCola y TPila
# Utilizar solo colas y pilas  para resolver el problema.
# No utilizar funciones de string para resolver el problema.

# Fecha limite de entrega 09/05/2021. Se debe entregar la resolución del problema en Python. Adjuntar solo el archivo .py con la resolución.

# PcrearC
# PllenaC
# PponerC
# PvaciaC
# PsacarC

# CcrearC
# CllenaC
# CponerC
# CvaciaC
# CsacarC

import imp
TPila = imp.load_compiled("TPila", "../lib/TPila.cpython-37.pyc")
TCola = imp.load_compiled("TCola", "../lib/TCola.cpython-37.pyc")
TDato = imp.load_compiled("TDato", "../lib/TDato.cpython-37.pyc")

separador = " "

p = TPila.TPilaC()
c = TCola.TColaC()
datoC = TDato.TdatoC()

def MostrarMensaje(mensaje, tipo = "Error"):
    print("¡" + tipo + ": " + mensaje + "!")

def IngresarPalabras(c):
    datoC.valor = input()
    while datoC.valor != "FIN" and not TCola.CllenaC(c):
        TCola.CponerC(c, datoC)
        datoC.valor = input()
    if datoC.valor != "FIN" and TCola.CllenaC(c):
        MostrarMensaje("La cola está llena y no soporta mas elementos.")
        MostrarMensaje("Se tratarán los elementos que pudieron ingresarse.", "Advertencia")


def OrdenarCola(entrada):
    c = TCola.TColaC()
    TCola.CcrearC(c)

    p1 = TPila.TPilaC()
    TPila.PcrearC(p1)
    p2 = TPila.TPilaC()
    TPila.PcrearC(p2)

    if not TCola.CvaciaC(entrada):
        TCola.CsacarC(entrada, datoC)
        tope = TDato.TdatoC()
        tope.valor = datoC.valor

        while (not TCola.CvaciaC(entrada)):
            TCola.CsacarC(entrada, datoC)
            
            if(len(datoC.valor) >= len(tope.valor)):
                TPila.PponerC(p1, tope)
                tope.valor = datoC.valor
            else:
                while(not TPila.PvaciaC(p1) and len(datoC.valor) < len(tope.valor)):
                    TPila.PponerC(p2, tope)
                    TPila.PsacarC(p1, tope)
                TPila.PponerC(p1, datoC)
                while(not TPila.PvaciaC(p2)):
                    TPila.PsacarC(p2, datoC)
                    TPila.PponerC(p1, datoC)
                TPila.PsacarC(p1, tope)
        while(not TPila.PvaciaC(p1)):
            TPila.PsacarC(p1, datoC)
            TCola.CponerC(c, datoC)
        TCola.CponerC(c, tope)
    return c

def InvertirPalabra(palabra):
    p = TPila.TPilaC()
    TPila.PcrearC(p)
    i = 0
    while i < len(palabra) and not TPila.PllenaC(p):
        datoC.valor = palabra[i]
        TPila.PponerC(p, datoC)
        i = i + 1
    return p
    
def MostrarPalabraInvertida(palabra):
    p = InvertirPalabra(palabra)
    while not TPila.PvaciaC(p):
        TPila.PsacarC(p, datoC)
        print(datoC.valor, end="")
    print(" ", end="")

def MostrarCola(c):
    while not TCola.CvaciaC(c):
        TCola.CsacarC(c, datoC)
        MostrarPalabraInvertida(datoC.valor)

IngresarPalabras(c)
c = OrdenarCola(c)
MostrarCola(c)
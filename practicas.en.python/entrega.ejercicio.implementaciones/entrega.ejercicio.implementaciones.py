# Realizar las implementaciones de PILAS DINAMICAS y COLAS LINEALES DINAMICAS, y verificar que el programa de aplicación de pilas y colas funciona igual, sin tener que realizar cambios en el mismo.

# Además deberán entregar la implementación de LISTAS ESTATICAS CON CORRIMIENTOS y de las LISTAS DOBLES CIRCULARES.

# Fecha limite de entrega 08/06/2021. Se debe entregar la resolución del problema y los fuentes de los módulos de las implementaciones pedidas en Python. Adjuntar solo los archivos .py con la resolución.

import imp
TPila = imp.load_source("TPila", "./tPila.py")
TCola = imp.load_source("TCola", "./tCola.py")
# TLista = imp.load_source("TLista", "./tLista.py")
TLista = imp.load_source("TLista", "./tListaD.py")
TDato = imp.load_compiled("TDato", "../lib/TDato.cpython-37.pyc")

p = TPila.TPilaC()
c = TCola.TColaC()
datoC = TDato.TdatoC()

TPila.PcrearC(p)

datoC.valor = 'a'
TPila.PponerC(p, datoC)
datoC.valor = 'b'
TPila.PponerC(p, datoC)
datoC.valor = 'c'
TPila.PponerC(p, datoC)

while not(TPila.PvaciaC(p)):
    TPila.PsacarC(p, datoC)
    print(datoC.valor)

TCola.CcrearC(c)

datoC.valor = 'a'
TCola.CponerC(c, datoC)
datoC.valor = 'b'
TCola.CponerC(c, datoC)
datoC.valor = 'c'
TCola.CponerC(c, datoC)

while not(TCola.CvaciaC(c)):
    TCola.CsacarC(c, datoC)
    print(datoC.valor)

l = TLista.TListaC()
TLista.lCrear(l)
if(TLista.lVacia(l)):
    print("Vacía")


a = TLista.TDatoL('a')
TLista.lInsertarPpio(l, a)
b = TLista.TDatoL('b')
TLista.lInsertarPpio(l, b)
d = TLista.TDatoL('d')
TLista.lInsertarPpio(l, d)

# TLista.lInsertarFin(l, '0')
# TLista.lInsertarFin(l, '1')
# TLista.lInsertarFin(l, '2')

# TLista.lBorrarPpio(l)

# TLista.lBorrarFin(l)
# TLista.lBorrarFin(l)
# TLista.lBorrarFin(l)

# TLista.lPpio(l)
# datoC.valor = '3'
# TLista.lModificar(l, datoC)

c = TLista.TDatoL('c')
TLista.lInsertarOrden(l, c, 'D')

# TLista.lPpio(l)
# TLista.lBorrarActual(l)

datoC.valor = False
TLista.lBuscar(l, 'b', datoC)
TLista.lBuscar(l, 'x', datoC)

print("End")
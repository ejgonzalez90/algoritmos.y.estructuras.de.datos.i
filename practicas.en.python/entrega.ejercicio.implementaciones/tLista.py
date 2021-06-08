max = 200

class TDatoL:
    def __init__(self, clave = None) -> None:
        self.clave = clave

class TListaC:
    def __init__(self) -> None:
        self._arregloLista = [None] * max
        self._actual = -1
        self._tope = -1

def lVacia(l):
    return l._tope == -1

def lPpio(l):
    l._actual = 0

def lInfo(l, x):
    x = l._arregloLista[l._actual]

def lSig(l):
    l._actual = l._actual + 1

def lFin(l):
    return l._actual == l._tope

def lLlena(l):
    return l.tope == max

def lCrear(l):
    l = TListaC()

def lInsertarPpio(l, x):
    for i in range(l._tope, -1, -1):
        l._arregloLista[i + 1] = l._arregloLista[i]
    l._arregloLista[0] = x
    l._tope = l._tope + 1

def lInsertarFin(l, x):
    if(l._actual == -1):
        l._actual = 0
    l._tope = l._tope + 1
    l._arregloLista[l._tope] = x

def lBorrarPpio(l):
    if(l._tope != 0):
        for x in range(0, l._tope):
            l._arregloLista[x] = l._arregloLista[x + 1]
    l._tope = l._tope - 1

def lBorrarFin(l):
    l._tope = l._tope - 1

def lModificar(l, x):
    l._arregloLista[l.actual] = x

def lInsertarOrden(l, x, tOrden):
    if l._tope == -1:
        l._arregloLista[0] = x
        l._actual = 0
        l._tope = 0
    else:
        i = 0
        while i < l._tope and ((tOrden == 'A' and l._arregloLista[i].clave < x.clave) or (tOrden == 'D' and l._arregloLista[i].clave > x.clave)):
            i = i + 1
        for k in range(l._tope, i - 1, -1):
            l._arregloLista[k + 1] = l._arregloLista[k]
        l._arregloLista[i] = x
        l._tope = l._tope + 1

def lBorrarActual(l):
    for x in range(l._actual, l._tope):
        l._arregloLista[x] = l._arregloLista[x + 1]
    l._tope = l._tope - 1

def lBuscar(l, k, existe):
    existe.valor = False    
    asc = True
    if l._arregloLista[0].clave > l._arregloLista[l._tope].clave:
        asc = False
    prim = 1
    ult = l._tope
    while prim <= ult and not(existe.valor):
        central = (prim + ult) // 2
        if(k == l._arregloLista[central].clave):
            existe.valor = True
            l._actual = central
        else:
            if (asc and k > l._arregloLista[central].clave) or (not(asc) and k < l._arregloLista[central].clave):
                prim = central + 1
            else:
                ult = central - 1
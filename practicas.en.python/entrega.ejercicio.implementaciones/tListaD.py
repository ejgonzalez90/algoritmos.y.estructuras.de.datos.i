class TDatoL:
    def __init__(self, clave = None) -> None:
        self.clave = clave

class TNodo:
    def __init__(self, info = None) -> None:
        self._info = info
        self._ant = None
        self._sig = None

class TListaC:
    def __init__(self) -> None:
        self._cab = None
        self._actual = None

def lVacia(l):
    return l._cab == None

def lPpio(l):
    l._actual = l._cab

def lInfo(l, x):
    x = l._actual._info

def lSig(l):
    l._actual = l._actual._sig

def lFin(l):
    return l._actual == l._cab

def lLlena(l):
    return False

def lCrear(l):
    l = TListaC()

def lInsertarPpio(l, x):
    nue = TNodo(x)
    if l._cab != None:
        nue._sig = l._cab
        nue._ant = l._cab._ant
        l._cab._ant._sig = nue
        l._cab._ant = nue
    else:
        nue._sig = nue
        nue._ant = nue
    l._cab = nue

def lInsertarFin(l, x):
    nue = TNodo(x)
    if l._cab != None:
        nue._sig = l._cab
        nue._ant = l._cab._ant
        l._cab._ant._sig = nue
        l._cab._ant = nue
    else:
        nue._sig = nue
        nue._ant = nue
        l._cab = nue

def lBorrarPpio(l):
    if l._cab == l._cab._sig:
        l._cab = None
    else:
        l._cab._ant._sig = l._cab._sig
        l._cab._sig._ant = l._cab._ant
        l._cab = l._cab._sig

def lBorrarFin(l):
    if l._cab == l._cab._sig:
        l._cab = None
    else:
        l._cab._ant._ant._sig = l._cab
        l._cab._ant = l._cab._ant._ant

def lModificar(l, x):
    l._actual._info = x

def lInsertarOrden(l, x, tOrden):
    nue = TNodo(x)
    if l._cab != None:
        aux = l._cab
        while (tOrden == "A" and aux._sig_info.clave < x.clave) or (tOrden == "D" and aux._sig._info.clave > x.clave):
            aux = aux._sig
        nue._sig = aux._sig
        nue._ant = aux
        aux._sig._sig._ant = nue
        aux._sig = nue
    else:
        l._cab = nue
        l._cab._sig = nue
        l._cab._ant = nue

def lBorrarActual(l):
    if(l._actual._sig == l._actual):
        l._cab = None
        l._actual = None
    else:
        l._actual._sig._ant = l._actual._ant
        l._actual._ant._sig = l._actual._sig

def lBuscar(l, k, existe):
    existe.valor = False
    asc = True
    if l._cab._ant._info.clave < l._cab._info.clave:
        asc = False
    aux = l._cab
    while (asc and aux._info.clave < k) or (not(asc) and aux._info.clave > k):
        aux = aux._sig
    if aux._info.clave == k:
        existe.valor = True
        l._actual = aux

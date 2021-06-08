class TRegistro:
    def __init__(self, info = None) -> None:
        self.info = info
        self._sig = None

class TPilaC:
    def __init__(self) -> None:
        self.tope = None

def PcrearC(p):
    p = TPilaC()

def PllenaC(p) -> bool:
    return False

def PponerC(p, dato):
    nue = TRegistro(dato.valor)
    if p.tope != None:
        nue._sig = p.tope
    p.tope = nue

def PvaciaC(p):
    return p.tope == None

def PsacarC(p, dato):
    dato.valor = p.tope.info
    p.tope = p.tope._sig

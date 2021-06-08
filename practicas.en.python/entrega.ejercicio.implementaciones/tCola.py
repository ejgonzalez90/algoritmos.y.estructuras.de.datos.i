class TRegistro:
    def __init__(self, info = None) -> None:
        self.info = info
        self._sig = None

class TColaC:
    def __init__(self) -> None:
        self.frente = None

def CcrearC(c):
    c = TColaC()

def CllenaC(c):
    return False

def CponerC(c, dato):
    nue = TRegistro(dato.valor)
    if c.frente == None:
        c.frente = nue
    else:
        aux = c.frente
        while aux._sig != None:
            aux = aux._sig
        aux._sig = nue

def CvaciaC(c):
    return c.frente == None

def CsacarC(c, dato):
    dato.valor = c.frente.info
    c.frente = c.frente._sig

class ElementoFila():
    def __init__(self, Ivalor, Iprioridade):
        self.valor = Ivalor
        self.anterior = None
        self.prioridade = int(Iprioridade)


class Fila():
    def __init__(self):
        self.primeiroElementodFila = None
        self.ultimoElementoFila = None
    x = 0

    def enfileira(self, valor, prioridade):
        novoElementoFila = ElementoFila(valor, prioridade)
        elementoAtual = self.primeiroElementodFila
        while elementoAtual.anterior != None:
            if 


            elementoAtual = elementoAtual.anterior
        if self.ultimoElementoFila != None:
            self.ultimoElementoFila.anterior = novoElementoFila
        self.ultimoElementoFila = novoElementoFila
        if self.primeiroElementodFila == None:
            self.primeiroElementodFila = self.ultimoElementoFila
        self.x += 1

    def desenfileira(self):
        if self.primeiroElementodFila == None:
            self.ultimoElementoFila = None
            return None
        elementoFilaRemovido = self.primeiroElementodFila
        self.primeiroElementodFila = elementoFilaRemovido.anterior
        return elementoFilaRemovido.valor


s = input()


def separa_(s):
    x = 0
    listaS = []
    pos = s.index(" ")
    while True:
        if s.count(" ") == 1:
            listaS.append(s)
            return listaS
        else:
            listaS.append(s[:s.index(" ", pos+1)])
            pos = s.index(" ", pos+1)+1
            s = s[pos:]
            pos = s.index(" ")


listaS = []
for elem in separa_(s):
    listaS.append(elem.split())

filaPrioridade = Fila()

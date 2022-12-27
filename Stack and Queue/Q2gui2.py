class ElementoFila():
    def init(self, Ivalor, Iprioridade):
        self.valor = Ivalor
        self.anterior = None
        self.prioridade = int(Iprioridade)


class Fila():
    def init(self):
        self.primeiroElemento = None

    def enfileira(self, valor, prioridade):
        novoElemento = ElementoFila(valor, prioridade)
        if self.primeiroElemento == None:
            self.primeiroElemento = novoElemento
            return
        if self.primeiroElemento.prioridade > novoElemento.prioridade:
            novoElemento.anterior = self.primeiroElemento
            self.primeiroElemento = novoElemento
            return
        elementoAtual = self.primeiroElemento
        while elementoAtual.anterior != None:
            if novoElemento.prioridade <= elementoAtual.prioridade:
                break
            elementoAtual = elementoAtual.anterior
        novoElemento.anterior = elementoAtual.anterior
        elementoAtual.anterior = novoElemento

    def desenfileira(self):
        if self.primeiroElemento == None:
            return None
        elementoFilaRemovido = self.primeiroElemento
        self.primeiroElemento = elementoFilaRemovido.anterior
        return elementoFilaRemovido

    def print(self):
        elementoAtual = self.primeiroElemento
        while elementoAtual != None:
            print(elementoAtual.valor, elementoAtual.prioridade)
            elementoAtual = elementoAtual.anterior


s = input()
total = input()


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


fila = Fila()
for elem in separa_(s):
    fila.enfileira(elem[0], elem[1])

while total > 0:
    total -= 1
    fila.desenfileira()

while total == 0:
    print(f"Atividade: {elemento.valor}, Prioridade: #{lemento.prioridade}")


fila.print()

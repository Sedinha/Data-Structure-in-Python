class ElementoFila():
    def __init__(self, Ivalor, Iprioridade):
        self.valor = Ivalor
        self.anterior = None
        self.proximo = None
        self.prioridade = int(Iprioridade)


class Fila():
    def __init__(self):
        self.primeiroElemento = None

    def enfileira(self, valor, prioridade):
        novoElemento = ElementoFila(valor, prioridade)
        if self.primeiroElemento == None:
            self.primeiroElemento = novoElemento
        else:
            elementoAtual = self.primeiroElemento
            while True:
                if novoElemento.prioridade < elementoAtual.prioridade:
                    novoElemento.anterior = elementoAtual
                    novoElemento.proximo = elementoAtual.proximo
                    if elementoAtual.proximo != None:
                        elementoAtual.proximo.anterior = novoElemento
                        elementoAtual.proximo = novoElemento
                    else:
                        elementoAtual.proximo = novoElemento
                    if elementoAtual == self.primeiroElemento:
                        self.primeiroElemento = novoElemento
                    return
                if elementoAtual.anterior == None:
                    novoElemento.proximo = elementoAtual
                    elementoAtual.anterior = novoElemento
                    return
                elementoAtual = elementoAtual.anterior

    def desenfileira(self):
        if self.primeiroElemento == None:
            return None
        elementoFilaRemovido = self.primeiroElemento
        self.primeiroElemento = elementoFilaRemovido.anterior
        return elementoFilaRemovido


s = input()
s = s.strip()
total = int(input())


def separa_(s):
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
fila = Fila()
x = 0
for elem in separa_(s):
    listaS.append(elem.split())
    fila.enfileira(listaS[x][0], listaS[x][1])
    x += 1
print(f"Tamanho da fila: {len(listaS)-total}")
done = False
while not done:
    elemento = fila.desenfileira()
    total -= 1
    done = elemento == None
    if elemento != None and total < 0:
        print(
            f"Atividade: {elemento.valor}, Prioridade: #{elemento.prioridade}")

class ElementoPilha():
    def __init__(self, valorInicial):
        self.valor = valorInicial
        self.anterior = None


class Pilha():
    def __init__(self):
        self.elementoPilha = None

    def empilha(self, valor):
        novoElementoPilha = ElementoPilha(valor)
        if self.elementoPilha is not None:
            novoElementoPilha.anterior = self.elementoPilha
        self.elementoPilha = novoElementoPilha

    def desempilha(self):
        if self.elementoPilha is None:
            return None
        elementoPilhaRemovido = self.elementoPilha
        self.elementoPilha = elementoPilhaRemovido.anterior
        return elementoPilhaRemovido.valor


pilha = Pilha()
print(pilha.desempilha())
pilha.empilha(1)
pilha.empilha(2)
print(pilha.desempilha())
pilha.empilha(3)
print(pilha.desempilha())
print(pilha.desempilha())
print(pilha.desempilha())

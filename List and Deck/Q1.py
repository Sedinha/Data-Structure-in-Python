class ElementodLista():
    def __init__(self, valorInicial):
        self.valor = valorInicial
        self.proximo = None


class Lista():
    def __init__(self):
        self.firstElement = None
        self.lastElement = None

    def searchElePosição(self, posição):
        elePosi = self.firstElement
        posicaoSearch = 0
        while posicaoSearch != posição:
            if elePosi == None:
                return print(f"Posição não existente na lista: {posição}")
            if elePosi.proximo == None and posição == -1:
                return elePosi
            if elePosi.proximo.proximo == None and posição == -2:
                return elePosi
            elePosi = elePosi.proximo
            posicaoSearch += 1
        return elePosi

    def appendValor(self, valor, posição=0):
        newElmLista = ElementodLista(valor)

        if posição == -1 and self.firstElement == None:
            self.firstElement = newElmLista
            self.lastElement = newElmLista
            return None

        if posição == 0:
            if self.firstElement != None:
                newElmLista.proximo = self.firstElement
            else:
                self.lastElement = newElmLista
            self.firstElement = newElmLista
        elif posição == -1:
            self.lastElement.proximo = newElmLista
            self.lastElement = newElmLista

        else:
            elemPosi = self.searchElePosição(posição-1)
            newElmLista.proximo = elemPosi.proximo
            elemPosi.proximo = newElmLista
            return None

    def popElem(self, posição=0):
        if posição == 0:
            if self.firstElement == None:
                return None
            else:
                popElem = self.firstElement
                self.firstElement = self.firstElement.proximo
                if self.firstElement == None:
                    self.lastElement = None
                return popElem.valor
        else:
            if posição == -1 and self.firstElement == self.lastElement:
                popElem = self.firstElement
                self.firstElement = None
                self.lastElement = None
                return popElem
            elemPosi = self.searchElePosição(posição-1)
            if elemPosi.proximo != None:
                popElem = elemPosi.proximo
                elemPosi.proximo = popElem.proximo
                return popElem.valor
            return None

    def janelaAnalisada(self, l):
        maiorValor = 0
        jan = 1
        elem = self.firstElement
        if jan == l:
            return elem.valor
        while jan < l:
            if elem.proximo == None:
                return maiorValor
            if jan == 1:
                if elem.valor > elem.proximo.valor:
                    maiorValor = elem.valor
            else:
                if elem.valor > maiorValor and (elem.valor > elem.proximo.valor):
                    maiorValor = elem.valor
                else:
                    if maiorValor > elem.proximo.valor:
                        pass
                    else:
                        maiorValor = elem.proximo.valor
            elem = elem.proximo
            jan += 1
        return maiorValor


lista = Lista()
n = int(input())


def ajustaLista(nLista, kvezes):
    resposta = ""
    y = 0
    while y < ((nLista-kvezes)+1):
        r = str(lista.janelaAnalisada(kvezes))
        if resposta == "":
            resposta += r
        else:
            resposta += "  " + r
        lista.popElem()
        y += 1
    return print(resposta)


inputQuestao = input().split()
inputQuestao = [int(i) for i in inputQuestao]

x = 0
while x < n:
    lista.appendValor(inputQuestao[x], -1)
    x += 1

k = int(input())
if 1 <= k and k <= n:
    ajustaLista(n, k)

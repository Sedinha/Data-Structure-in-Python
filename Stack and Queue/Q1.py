class Anilha():
    def __init__(self, pesoA):
        self.peso = pesoA
        self.anterior = None


class PilhaAnilha():
    def __init__(self):
        self.anilhaFila = None

    x = 0
    pesoTotal = 0

    def empilhaAnilha(self, fpeso):
        novaAnilha = Anilha(fpeso)
        if self.anilhaFila != None:
            novaAnilha.anterior = self.anilhaFila
        self.anilhaFila = novaAnilha

    def desempilhaAnilha(self):
        if self.anilhaFila == None:
            return None
        anilhaRemovida = self.anilhaFila
        self.anilhaFila = anilhaRemovida.anterior
        self.x += 1
        self.pesoTotal += anilhaRemovida.peso
        pLista = [anilhaRemovida.peso, self.x, self.pesoTotal]
        return pLista


p_anilha = PilhaAnilha()
while True:
    peso = int(input())
    if peso == 0:
        break
    p_anilha.empilhaAnilha(peso)

pesoDesejado = int(input())
while p_anilha.anilhaFila.peso != pesoDesejado:
    pRetirado = p_anilha.desempilhaAnilha()
    pRetirado
    print("Peso retirado:", pRetirado[0])

if p_anilha.anilhaFila.peso == pesoDesejado:
    pRetirado = p_anilha.desempilhaAnilha()
    pRetirado
    print("Peso retirado:", pRetirado[0])
    print("Anilhas retiradas:", pRetirado[1])
    print("Peso total movimentado:", pRetirado[2])

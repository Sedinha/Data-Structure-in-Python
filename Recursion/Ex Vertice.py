class Vertice():
    def __init__(self,nome):
        self.nome = nome
        self.verticesConectados = []

    def adicionarVerticeConectado(self,NovoVertice,distancia):
        self.verticesConectados.append((NovoVertice,distancia))
        NovoVertice.verticesConectados.append((self,distancia))

    def apagarConexao(self,vertice):
        for (verticeConectado,distancia) in self.verticesConectados:
            if verticeConectado == vertice:
                self.verticesConectados.remove((verticeConectado,distancia))
                verticeConectado.verticesConectados.remove((self,distancia))
                break
        del self
    
bel = Vertice("BEL")
bsb = Vertice("BSB")
bel.adicionarVerticeConectado(bsb,1600)
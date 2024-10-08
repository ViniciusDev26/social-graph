class Grafo:
    def __init__(self):
        self.grafo = {}  # Lista de adjacências
        self.vertices = set()  # Conjunto para armazenar todos os vértices

    # Função para adicionar uma aresta ao grafo
    def adicionar_aresta(self, v: str, w: str):
        if v not in self.grafo:
            self.grafo[v] = []

        self.grafo[v].append(w)
        self.vertices.add(v)
        self.vertices.add(w)

    # Função que faz uma DFS a partir de um vértice e marca os vértices visitados
    def _dfs(self, v: str, visitado: set, componente_atual: list):
        visitado.add(v)
        componente_atual.append(v)

        for i in self.grafo[v]:
            if i not in visitado:
                self._dfs(i, visitado, componente_atual)

    # Função para preencher a pilha de acordo com a ordem de finalização da DFS
    def _preencher_ordem(self, v: str, visitado: set, pilha: list):
        visitado.add(v)

        for i in self.grafo[v]:
            if i not in visitado:
                self._preencher_ordem(i, visitado, pilha)

        pilha.append(v)

    # Função para obter o grafo transposto (inverter as arestas)
    def _grafo_transposto(self):
        g_t = Grafo()

        for v in self.grafo:
            for w in self.grafo[v]:
                g_t.adicionar_aresta(w, v)

        return g_t

    # Função principal para encontrar e retornar todos os SCCs
    def kosaraju(self):
        pilha = []
        visitado = set()

        # Passo 1: Fazer uma DFS e preencher a pilha com a ordem de finalização
        for v in self.vertices:
            if v not in visitado:
                self._preencher_ordem(v, visitado, pilha)

        # Passo 2: Inverter o grafo
        g_t = self._grafo_transposto()

        # Passo 3: Fazer DFS no grafo transposto na ordem inversa de finalização
        visitado.clear()
        componentes_fortemente_conectados = []

        while pilha:
            v = pilha.pop()
            if v not in visitado:
                componente_atual = []
                g_t._dfs(v, visitado, componente_atual)
                componentes_fortemente_conectados.append(componente_atual)

        return componentes_fortemente_conectados

    # Função para verificar se uma aresta já existe
    def existe_aresta(self, u: str, v: str) -> bool:
        return v in self.grafo[u]

g = Grafo()
g.adicionar_aresta("Ana", "Bia")
g.adicionar_aresta("Bia", "Pedro")
g.adicionar_aresta("Pedro", "Ana")
g.adicionar_aresta("Bia", "Lucas")
g.adicionar_aresta("Lucas", "Ana")
g.adicionar_aresta("Lucas", "Joao")
g.adicionar_aresta("Joao", "Ze")
g.adicionar_aresta("Ze", "Bruna")
g.adicionar_aresta("Bruna", "Joao")

print("Componentes Fortemente Conectados (SCCs):")
sccs = g.kosaraju()
for i, scc in enumerate(sccs, 1):
    print(f"SCC {i}: {scc}")

    # Sugestão de amizades:
    if len(scc) == 1:
        print(f"Sugestão de amizade: {scc[0]} -> {scc[0]}")
    else:
        for u in scc:
            for v in scc:
                if u != v and not g.existe_aresta(u, v):
                    print(f"Sugestão de amizade: {u} -> {v}")

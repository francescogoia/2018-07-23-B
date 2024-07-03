import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMap = {}
        self._grafo = nx.Graph()
        self._years = DAO.getAllYears()

    def _crea_grafo(self, giorni, anno):
        self._grafo.clear()
        self._nodes = DAO.getAllStates()
        self._grafo.add_nodes_from(self._nodes)
        allEdges = DAO.getAllEdges()
        edgesPeso = DAO.getAllEdgesPeso(giorni, anno)
        for e in allEdges:
            self._grafo.add_edge(e[0], e[1], weight=0)
        for e in edgesPeso:
            self._grafo[e[0]][e[1]]["weight"] = e[2]

    def get_dettagli_grafo(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def get_peso_adiacenti(self):
        result = []
        for n in self._nodes:
            peso_adiacenti = 0
            for v in self._grafo.neighbors(n):
                peso_adiacenti += self._grafo[n][v]["weight"]
            result.append((n, peso_adiacenti))
        return result

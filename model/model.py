import networkx as nx

from database.DAO import DAO
from model.circuit import Circuit
from model.piazzamento import Piazzamento


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._IDMap = {}

    def getAnni(self):
        return DAO.getAllYears()

    def creaGrafo(self, start, end):
        self._grafo.clear()
        self._IDMap = {}

        circuiti = DAO.getAllCircuits()
        nodi = []

        for c in circuiti:
            id = c['circuitId']

            piazzamenti = DAO.getPiazzamento(id, start, end)

            corretto= {}
            for p in piazzamenti:
                if p['year'] not in corretto:
                    corretto[p['year']] = []
                corretto[p['year']].append(Piazzamento(p['driverId'], p['position']))

            circuito = Circuit(c['circuitId'], c['circuitRef'], c['name'],
                               c['location'], c['country'], c['lat'],
                               c['lng'], c['alt'], c['url'], corretto)
            nodi.append(circuito)
            self._IDMap[circuito.circuitId] = circuito

        self._grafo.add_nodes_from(nodi)

        archi = DAO.getArchi(start, end, self._IDMap)
        pesi = {}
        for a in archi:
            u = a[0]
            v = a[1]
            if u.circuitId in pesi:
                pesoU = pesi[u.circuitId]
            else:
                pesoU = self._calcolaPeso(u)
                pesi[u.circuitId] = pesoU
            if v.circuitId in pesi:
                pesoV = pesi[v.circuitId]
            else:
                pesoV = self._calcolaPeso(v)
                pesi[v.circuitId] = pesoV

            self._grafo.add_edge(u,v,weight=(pesoU+pesoV))

    def _calcolaPeso(self, u):

        peso = 0

        posizionamenti = u.piazzamenti
        for k,v in posizionamenti.items():
            for d in v:
                if d.position is not None:
                    peso += 1

        return peso



    def getInfo(self):
        return len(self._grafo.nodes()), len(self._grafo.edges())

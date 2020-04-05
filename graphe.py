import copy
from collections import deque

from lien import Lien
from noeud import Noeud


class Graphe:
    def __init__(self, IdentifiantGraphe):
        self.__idGraphe = IdentifiantGraphe
        self._numberNoeuds = 0
        self._dic_Noeuds = {}
        self._dic_Liens = {}

    def __str__(self):
        print("\nListe des Noeuds : "+str(self._dic_Noeuds))
        print("\nListe des Liens : "+str(self._dic_Liens))

    def getNumberNoeud(self):
        return self._numberNoeuds

    def ajouterNoeud(self, node):
        self._dic_Noeuds[node.getId_Noeud()] = node
        self._numberNoeuds += 1

    def ajouterLien(self, lien):
        self._dic_Liens[lien.getId_Lien()] = lien
        self._dic_Noeuds[lien.getNoeud1()].ajouterIdentifiantLien(lien.getId_Lien())
        self._dic_Noeuds[lien.getNoeud2()].ajouterIdentifiantLien(lien.getId_Lien())

    def obtenirProchainsNoeuds2(self, IdentifiantNoeud):
        dicProchainsNoeuds = {}

        for link_id in self._dic_Liens:
            link_id1=link_id
            link_id=link_id.split(".")
            if link_id[0] == str(IdentifiantNoeud):
                dicProchainsNoeuds[link_id[1]] = self._dic_Liens[link_id1].getDistance()
            if link_id[1] == str(IdentifiantNoeud):
                dicProchainsNoeuds[link_id[0]] = self._dic_Liens[link_id1].getDistance()

        return dicProchainsNoeuds

    def dijkstraAlgo(self, idNoeudS, idNoeudD):
        P = list()
        d = {}
        keyMin = 0
        for i in range(1, self._numberNoeuds+1):
            d[i] = float('inf')
        d[idNoeudS] = 0

        while not len(P) == self._dic_Noeuds:
            D = copy.deepcopy(d)
            for i in range(1, len(d)):
                print(self._dic_Noeuds[i].getId_Noeud())
                if self._dic_Noeuds[i].getId_Noeud() in P:
                    del D[i]
            dMin = min(D.values())
            find = 0
            for idD in D:
                if dMin == D[idD] and not find:
                    keyMin = idD
                    find = 1

            print("Keymin " +str(self._dic_Noeuds[keyMin].getId_Noeud()))
            P.append(self._dic_Noeuds[keyMin].getId_Noeud())
            if not self._dic_Noeuds[keyMin].getId_Noeud() == idNoeudD:
                prNoeuds = self.obtenirProchainsNoeuds2(self._dic_Noeuds[keyMin].getId_Noeud())
                print(P)
                for key in prNoeuds:
                    print(type(key))
                    key=int(key)
                    print(str(self._dic_Noeuds[key].getId_Noeud()))

                    if not self._dic_Noeuds[2].getId_Noeud() in P:
                        distLien = prNoeuds[str(key)]
                        d[key] = min(d[key], (d[keyMin] + distLien))
            else:
                return P, d[keyMin]
        return P, d

    def dijkstra(self, sourceNode, destNode):

        assert sourceNode in self._dic_Noeuds, 'such source node does not exist'
        assert destNode in self._dic_Noeuds, 'such destination node does not exist'

        inf = float('inf')

        distances = {node: inf for node in self._dic_Noeuds}
        previous_nodes = {node: None for node in self._dic_Noeuds}
        distances[sourceNode] = 0

        nddict = self._dic_Noeuds.copy()
        nodes = set()
        for nd in nddict.keys():
            nodes.add(nd)

        while nodes:

            current_node = min(nodes, key=lambda node: distances[node])
            if distances[current_node] == inf:
                break

            for neighbour, cost in self.obtenirProchainsNoeuds2(current_node).items():
                alternative_route = distances[current_node] + cost
                if alternative_route < distances[int(neighbour)]:
                    distances[int(neighbour)] = alternative_route
                    previous_nodes[int(neighbour)] = current_node

            nodes.remove(current_node)

        path, current_node = deque(), destNode
        while previous_nodes[current_node] is not None:
            path.appendleft(current_node)
            current_node = previous_nodes[current_node]
        if path:
            path.appendleft(current_node)
        return path

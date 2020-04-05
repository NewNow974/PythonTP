from lien import Lien
from noeud import Noeud


class Graphe:
    def __init__(self, IdentifiantGraphe):
        self.__id = IdentifiantGraphe
        self._numberNoeuds = 0
        self._dic_Noeuds = {}
        self._dic_Liens = {}

    def __str__(self):
        print("\nNode : {0}".format(self._dic_Noeuds))
        print("\nLink : {0}".format(self._dic_Liens))

    def getNumberNoeud(self):
        return self._numberNoeuds

    def ajouterNoeud(self, node):
        self._dic_Noeuds[node.get_id()] = node
        self._numberNoeuds += 1

    def ajouterLien(self, lien):
        self._dic_Liens[lien.get_id()] = lien
        self._dic_Noeuds[lien.getNoeud1()].ajouterIdentifiantLien(lien.get_id())
        self._dic_Noeuds[lien.getNoeud2()].ajouterIdentifiantLien(lien.get_id())

    def obtenirProchainsNoeuds2(self, IdentifiantNoeud):
        next_nodes_dic = {}

        for link_id in self._dic_Liens:
            link_id1=link_id
            link_id=link_id.split(".")
            if link_id[0] == str(IdentifiantNoeud):
                next_nodes_dic[link_id[1]] = self._dic_Liens[link_id1].get_distance()
            if link_id[1] == str(IdentifiantNoeud):
                next_nodes_dic[link_id[0]] = self._dic_Liens[link_id1].get_distance()

        return next_nodes_dic


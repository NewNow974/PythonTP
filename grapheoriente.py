from graphe import Graphe
from lien import Lien
from noeud import Noeud


class OrientedGraphe(Graphe):
    def __init__(self, identify):
        Graphe.__init__(self, identify)

    def obtenirProchainsNoeudsOriente(self, identifiantNoeud):
        identifiantNoeud = str(identifiantNoeud)
        dic_prochainNoeud = {}

        for element in self._dic_Liens:
            element1 = element
            element = element.split("--")
            if element[0] == identifiantNoeud:
                dic_prochainNoeud[element1] = self._dic_Liens[element1].getNoeud2()

        return dic_prochainNoeud


noeud1 = Noeud(1)
noeud2 = Noeud(2)
noeud3 = Noeud(3)
noeud4 = Noeud(4)

lien1 = Lien(noeud1.getIdentifiantNoeud(), noeud2.getIdentifiantNoeud(), 10)
lien2 = Lien(noeud2.getIdentifiantNoeud(), noeud3.getIdentifiantNoeud(), 11)
lien3 = Lien(noeud3.getIdentifiantNoeud(), noeud4.getIdentifiantNoeud(), 11)
lien1.__str__()

g1 = Graphe(10)
g1.ajouterNoeud(noeud1)
g1.ajouterNoeud(noeud2)
g1.ajouterNoeud(noeud3)
g1.ajouterLien(lien1)
g1.ajouterLien(lien2)
g1.ajouterLien(lien3)

g1.__str__()

print("Prochaine Noeud est :" + str(g1.obtenirProchainsNoeuds(noeud2.getIdentifiantNoeud())))
print("ICI")

g2 = OrientedGraphe(11)
g2.ajouterNoeud(noeud1)
g2.ajouterNoeud(noeud2)
g2.ajouterNoeud(noeud3)
g2.ajouterLien(lien1)
g2.ajouterLien(lien2)
g2.ajouterLien(lien3)

# print("Liste noeuds traversés : "+ str(g1.dijkstra(noeud1, noeud4)))

print("Prochaine Noeud Orienté est :" + str(g2.obtenirProchainsNoeudsOriente(noeud2.getIdentifiantNoeud())))

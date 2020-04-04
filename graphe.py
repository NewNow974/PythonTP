from lien import Lien
from noeud import Noeud


class Graphe:
    """Class Graphe"""

    """Initialize the value."""
    def __init__(self, identifiantGraphe):
        self._identifiantGraphe=identifiantGraphe
        self._numberNoeuds=0

        self._dic_Noeuds={}
        self._dic_Liens={}


    """Getters et Setterse"""
    def getIdentifiantGraphe(self):
        return self._identifiantGraphe

    """def setIdentifiantGraphe(self, identifiantGraphe):
        self.__identifiantGraphe=identifiantGraphe"""

    def getNumberNoeuds(self):
        return self._numberNoeuds


    """Les méthode"""
    def __str__(self):
        print("Noeud : " + str(self._dic_Noeuds) + "\n")
        print("Lien : " + str(self._dic_Liens) + "\n")

    def ajouterNoeud(self, noeud):
        self._dic_Noeuds[noeud.getIdentifiantNoeud()]=noeud
        self._numberNoeuds+=1


    def ajouterLien(self, lien):
        self._dic_Liens[lien.getIdentifiantLien()]=lien

    def obtenirProchainsNoeuds(self, identifiantNoeud):
        identifiantNoeud=str(identifiantNoeud)
        dic_prochainNoeud={}

        for element in self._dic_Liens:
            if element[0]  in identifiantNoeud:
                dic_prochainNoeud[element]=self._dic_Liens[element].getNoeud2()

        return dic_prochainNoeud



"""noeud1 = Noeud()
noeud2 = Noeud()
noeud3 = Noeud()


lien1 = Lien(noeud1.getIdentifiantNoeud(),noeud2.getIdentifiantNoeud(), 10)
lien2 = Lien(noeud1.getIdentifiantNoeud(),noeud3.getIdentifiantNoeud(), 11)
lien1.__str__()

g1 = Graphe(10)
g1.ajouterNoeud(noeud1)
g1.ajouterNoeud(noeud2)
g1.ajouterNoeud(noeud3)
g1.ajouterLien(lien1)
g1.ajouterLien(lien2)
g1.__str__()

print("Prochaine Noeud est :"+str(g1.obtenirProchainsNoeuds(noeud1.getIdentifiantNoeud())))


print("ICI")"""




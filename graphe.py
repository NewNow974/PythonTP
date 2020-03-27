from noeud import Noeud
from lien import Lien


class Graphe(Noeud):
    """Class Graphe"""

    """Initialize the value."""
    def __init__(self, identifiantGraphe):
        self._identifiantGraphe=identifiantGraphe
        self._numberNoeuds=0
        self._dictionnaireNoeuds={}
        self._dictionnaireLiens={}


    """Getters et Setterse"""
    def getIdentifiantGraphe(self):
        return self._identifiantGraphe

    def setIdentifiantGraphe(self, identifiantGraphe):
        self._identifiantGraphe=identifiantGraphe

    def getNumberNoeuds(self):
        return self._numberNoeuds


    """Les méthode"""
    def __str__(self):
        print("L'identifiant du Noeud est : "+ str(self._identifiantGraphe))

    def ajoutNoeudToGraph(self, noeud):
        self._dictionnaireNoeuds.add(noeud)
        self._numberNoeuds+=1

    def ajoutLienToGraph(self, lien):
        self._dictionnaireLiens.add(lien)

    def obtenirProchainsNoeuds(self, identifiantNoeud):
        self._liste.append()







from lien import Lien
from noeud import Noeud


class Graphe:
    """Class Graphe"""

    """Initialize the value."""

    def __init__(self, identifiantGraphe):
        self._identifiantGraphe = identifiantGraphe
        self._numberNoeuds = 0

        self._dic_Noeuds = {}
        self._dic_Liens = {}

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
        self._dic_Noeuds[noeud.getIdentifiantNoeud()] = noeud
        self._numberNoeuds += 1

    def ajouterLien(self, lien):
        self._dic_Liens[lien.getIdentifiantLien()] = lien

    def obtenirProchainsNoeuds(self, identifiantNoeud):
        identifiantNoeud = str(identifiantNoeud)
        dic_prochainNoeud = {}

        for element in self._dic_Liens:
            element1 = element
            element = element.split("--")
            if element[0] == identifiantNoeud:
                dic_prochainNoeud[element1] = self._dic_Liens[element1].getNoeud2()
            if element[1] == identifiantNoeud:
                dic_prochainNoeud[element1] = self._dic_Liens[element1].getNoeud1()

        return dic_prochainNoeud

    def obtenirProchainsNoeuds2(self, identifiantNoeud):
        dic_prochainNoeud = {}

        listLiens = self._dic_Liens  # Utilisation du dico Lien pour trouver les prochain Neoud
        compteur = 0

        for element in listLiens:
            print("Element " + element)
            print("idNoeud " + str(identifiantNoeud))
            if identifiantNoeud == element.getNoeud2().getIdentifiantNoeud():  #

                idNoeudA = self._dic_Liens[element].getNoeud2()
                dic_prochainNoeud[compteur] = idNoeudA
                compteur += 1

        return dic_prochainNoeud



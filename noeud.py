from lien import Lien

class Noeud(Lien):
    """Class Noeud"""
    id = 1

    """Initialize the value."""
    def __init__(self):
        self._identifiantNoeud=self.getId()
        self._liste=[]

        Noeud.id+=1

    """Getters et Setterse"""
    def getIdentifiantNoeud(self):
        return self._identifiantNoeud

    def setIdentifiantNoeud(self, identifiantNoeud):
        self._identifiantNoeud=identifiantNoeud

    def getListe(self):
        for element in self._liste:
            print(element)
        """return self.__liste"""


    """Les méthode"""
    def __str__(self):
        print("L'identifiant du Noeud est : " + str(self._identifiantNoeud))

    def affichageIdentifiantLien(self):
        print("Liste des liens : " + str(self.getListe()))

    def ajoutIdentifiantLien(self, identifiant):
        self._liste.append(identifiant)




    @classmethod
    def getId(cls):
        return Noeud.id


noeud1= Noeud()
noeud1.__str__()
noeud1.affichageIdentifiantLien()

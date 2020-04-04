

class Noeud:
    """Class Noeud"""
    id = 1

    """Initialize the value."""
    def __init__(self,idNoeud):
        """self.__identifiantNoeud=self.getId()"""
        self.__identifiantNoeud=idNoeud
        self.__liste=[]



    """Getters et Setterse"""
    def getIdentifiantNoeud(self):
        return self.__identifiantNoeud

    def setIdentifiantNoeud(self, identifiantNoeud):
        self.__identifiantNoeud=identifiantNoeud


    """Les méthode"""
    def __str__(self):
        print("L'identifiant du Noeud est : " + str(self.__identifiantNoeud))

    """def affichageIdentifiantLien(self):
        print("Liste des liens : " + str(self.getListe()))"""

    def ajoutIdentifiantLien(self, identifiant):
        self.__liste.append(identifiant)

    def affichageIdentifiantLien(self):
        print(self.__liste)


    @classmethod
    def getId(cls):
        return Noeud.id



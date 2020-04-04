from noeud import Noeud


class Lien:
    """Class Lien"""

    def __init__(self, noeud1, noeud2, distance):
        """Initialize the value."""
        self.__identifiant= str(noeud1) +"--"+ str(noeud2)
        self.__distance=distance
        self.__noeud1=noeud1
        self.__noeud2=noeud2


    def getIdentifiantLien(self):
        return self.__identifiant

    def getDistance(self):
        return self.__distance

    def getNoeud1(self):
        return self.__noeud1

    def getNoeud2(self):
        return self.__noeud2

    def setIdentifiant(self, identifiant):
        self.__identifiant=identifiant


    def __str__(self):
        print("L'identifiant du lien est : " + str(self.getIdentifiantLien()))
        print("La distance du lien est : " + str(self.getDistance()))



class Lien:
    """Class Lien"""

    def __init__(self, noeud1, noeud2, distance):
        """Initialize the value."""
        self._identifiant=0
        self.__distance=distance
        self.__noeud1=noeud1
        self.__noeud2=noeud2


    def getIdentifiant(self):
        return self._identifiant

    def getDistance(self):
        return self.__distance

    def getNoeud1(self):
        return self.__noeud1

    def getNoeud2(self):
        return self.__noeud2

    def setIdentifiant(self, identifiant):
        self._identifiant=identifiant


    def __str__(self):
        print("L'identifiant est : " + str(self.getIdentifiant()))
        print("La distance du lien est : " + str(self.getDistance()))

Lien1 = Lien(1,1, 10)
Lien1.__str__()

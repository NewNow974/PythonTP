class Lien :
    def __init__(self, Noeud1, Noeud2, distance):
        self.__id = str(Noeud1) + "." +str(Noeud2)
        self.__noeud1 = Noeud1
        self.__noeud2 = Noeud2
        self.__distance = distance

    def __str__(self):
        print(self.__id)

    def get_id(self):
        return self.__id

    def getNoeud1(self):
        return self.__noeud1

    def getNoeud2(self):
        return self.__noeud2

    def get_distance(self):
        return self.__distance

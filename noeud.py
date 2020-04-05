class Noeud:
    def __init__(self, identifiantNoeud):
        self.__id = identifiantNoeud
        self.__connected_link = []

    def __str__(self):
        print(self.__id)

    def show_links_id(self):
        print(self.__connected_link)

    def ajouterIdentifiantLien(self, identify):
        self.__connected_link.append(identify)

    def get_id(self):
        return self.__id

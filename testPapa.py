# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:31:09 2020
énoncé :
Définir une classe qui implémente un TAD Liste non mutable fournissant les opérations suivantes :

création d’une liste vide
longueur
contient qui vérifie si un élément est dans la liste
affichage d’une liste sous la forme Python : [e0, e1, ... ]
ajout d’un élément en tête / en queue / en position k
accès à l’élément en tête / en queue / en position k
modification de l’élément en tête / en queue / en position k
suppression de l’élément en tête / en queue / en position k
concaténation de deux listes


"""

class Maillon:
    def __init__(self, element, suivant=None):
        self.contenu = element
        self.suivant = suivant

class ListeImmutable:
    def __init__(self):
        """Initialise une liste vide."""
        self._premier = None

    # une méthode qui duplique une liste
    def copie(self):
        res = ListeImmutable()
        courant = self._premier
        while not (courant == None):
            res = Maillon(courant, res)
            courant = courant.suivant
        return res

    def estVide(self):
        return self._premier == None

    def __len__(self):
        """Renvoie le nombre d'éléments présents dans la liste."""
        courant = self._premier
        lg = 0
        while not (courant == None):
            lg += 1
            courant = courant.suivant
        return lg

    def contenir(self, element) :
        courant = self._premier
        while not (courant == None):
            courant = courant.suivant
            if courant.contenu :
                return True
            return False

     def __str__(self):
        """ affichage d'une liste sous la forme python"""

        courant = self._premier
        print("[")
        while not (courant == None):
            print(courant.contenu, end=",")
            courant = courant.suivant
        print("]")

    def ajouteEnTete(self, element):
        """Insère elem en tête de liste en créant un nouveau maillon"""
        # On fait attention à maintenir un chaînage correcte :
        # la tête de la liste est modifiée, on met à jour _premier
        nouveau = Maillon(element)
        nouveau.suivant = self._premier
        self._premier = nouveau

    def supprimeTete(self):
        """Supprime l'élément en tête"""
        assert(not(self._premier  == None)) , "supprimeTete : erreur liste vide"
        self._premier = self._premier.suivant

    def tete(self):
        """Renvoie le contenu du premier maillon"""
        assert(not(self._premier  == None)) , "tete : erreur liste vide"
        return self._premier.contenu

    def kieme(self, k):
        """Renvoie le contenu du kieme maillon"""
        assert(k >= 0) , "kieme : erreur indice hors borne"
        courant = self._premier
        cpt = 0
        while cpt < k :
            assert(not(courant == None)) , "kieme : erreur indice hors borne"
            courant = courant.suivant
            cpt += 1
        assert(not(courant == None)) , "kieme : erreur indice hors borne"
        return courant.contenu

    def affecte(self, k, e):
        """Affecte le contenu du keme maillon avec l'élément e"""
        assert(k >= 0) , "kieme : erreur indice hors borne"
        courant = self._premier
        cpt = 0
        while cpt < k :
            assert(not(courant == None)) , "kieme : erreur indice hors borne"
            courant = courant.suivant
            cpt += 1
        assert(not(courant == None)) , "kieme : erreur indice hors borne"
        courant.contenu = e

    def queue(self):
        """Renvoie le dernier élément de la liste"""
        assert(not(self._premier  == None)) , "queue : erreur liste vide"
        courant = self._premier
        while not(courant.suivant == None):
            courant = courant.suivant
        return courant.contenu

    def ajouteEnQueue(self, element):
        """Ajoute un élément à la fin de la liste"""
        nouveau = Maillon(element)
        nouveau.suivant = None
        # Cas particulier de la liste vide : on modifie _premier
        if self._premier == None:
            self._premier = nouveau
        else:
            courant = self._premier
            while not(courant.suivant == None):
                courant = courant.suivant
            courant.suivant = nouveau

    def supprimeEnQueue(self):
         assert(not(self._premier  == None)) , " erreur liste vide"
        courant = self._premier
        res = self.copie()
        res._premier.suivant = res._premier
        return res
    # concaténer deux listes :

   def concatene(liste1, liste2):

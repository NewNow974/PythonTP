
from queue import PriorityQueue
from lien import Lien
from noeud import Noeud
from graphe import Graphe

import csv

"Lire le fichier"


def creationGraphe (idGraphe, fichier):
    with open(fichier) as csv_file:
        Graph = Graphe(idGraphe)

        f_csv = csv.reader(csv_file, delimiter='\t')

        header = next(f_csv)

        for i in range(int(header[0])):
            node = Noeud(i+1)
            Graph.ajouterNoeud(node)

        for ligne in f_csv:

            Graph.ajouterLien(Lien(ligne[0], ligne[1], ligne[2]))

    return Graph


graph=creationGraphe(1, "fileGraph1.csv")

graph.__str__()

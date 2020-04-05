from graphe import Graphe
from grapheoriente import GrapheOriente
from noeud import Noeud
from lien import Lien

import csv

def create_graph(graph_id, path_file) :
    with open(path_file, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')

        Graphe1 = GrapheOriente(graph_id)

        nb_node = next(reader)

        for i in range(1, int(nb_node[0])+1) :
            Graphe1.ajouterNoeud(Noeud(i))

        for row in reader:
            Graphe1.ajouterLien(Lien(int(row[0]), int(row[1]), float(row[2])))

        return Graphe1


#def dijkstra(id_node_source, id_node_dest):
#    nodes_list = []


noeud1 = Noeud(11)
noeud2 = Noeud(22)
noeud3 = Noeud(33)
noeud4 = Noeud(4444)

lien1 = Lien(11, 22, 10)
lien2 = Lien(22, 33, 11)

lien4 = Lien(11,4444,11)


g1 = GrapheOriente(10)
g1.ajouterNoeud(noeud1)

g1.ajouterNoeud(noeud2)
g1.ajouterNoeud(noeud3)
g1.ajouterNoeud(noeud4)
g1.ajouterLien(lien1)
g1.ajouterLien(lien2)
g1.ajouterLien(lien4)

print("Prochain Noeud")
print(g1.obtenirProchainsNoeuds(22))
print("===========================================================")
graph = create_graph(1, "fileGraph1.csv")
print("Liste prochaine Noeuds : " + str(graph.obtenirProchainsNoeuds(1)))


graph.__str__() #affichage liste

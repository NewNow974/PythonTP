from graphe import Graphe

class GrapheOriente(Graphe) :
    def __init__(self, IdentifiantGraphe):
        Graphe.__init__(self, IdentifiantGraphe)

    def obtenirProchainsNoeuds(self, IdentifiantNoeud):
        next_nodes_dic = {}

        for link_id in self._dic_Liens:
            link_id1=link_id
            link_id=link_id.split(".")
            if link_id[0] == str(IdentifiantNoeud):
                next_nodes_dic[link_id[1]] = self._dic_Liens[link_id1].get_distance()

        return next_nodes_dic

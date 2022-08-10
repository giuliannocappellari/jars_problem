class Graph:


    def __init__(self, adjac_lis:dict={}, final:dict={}) -> None:
        
        """
        adjac_lis: a dictionary of nodes and their adjacencies 
        final: a dictionary of nodes and their final values
        """
        self.adjac_lis = adjac_lis
        self.final = final


    def add_node(self, node:str, values:list) -> None:
        self.adjac_lis[node] = values
 

    def add_edge(self, node_1:str, node_2:str) -> None:
        self.adjac_lis[node_1].append(node_2)
        self.adjac_lis[node_2].append(node_1)   

    
    def get_node(self, node:str) -> list:
        return self.adjac_lis[node]


    def get_nodes(self) -> dict.keys():
        return self.adjac_lis.keys()    


    def get_edges(self) -> list:
        return self.adjac_lis.values()

    
    def get_adjac_lis(self) -> dict:
        return self.adjac_lis


    def create_jar(self, node:str) -> None:
        self.adjac_lis[node] = adjac_lis


    def get_combinations(self, node:dict):
        





g = Graph()
g.add_node(node='A', values=[5,7,8])

import graph
import networkx as nx

class JohnsonCycles:
    def __init__(self):
        self.blockedSet = set()
        self.blockedMap = {}
        self.stack = []
        self.allCycles = []

    def simpleCycles(self,studentGraph):
        startIndex = 1
        g = nx.DiGraph()
        #g.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 3)])
        g.add_edges_from(studentGraph.get_edges())
        scc = list(nx.strongly_connected_components(g)) # returns [{1,2,3}, {4,5}]
        print(scc)

if __name__ == "__main__":
    g = graph.Graph()
    g.add_student(1, "a", "b")
    g.add_student(2, "b", "c")
    g.add_student(3, "c", "a")
    g.add_student(4, "d", "e")
    g.add_student(5, "e", "d")
    print(g.get_edges())
    print(g.get_adjacency_dict())
    j = JohnsonCycles()
    j.simpleCycles(g)
class Digraph:
    """This class implements a directed graph with nodes represented by integers. """

    def __init__(self):
        """Initializes this digraph."""
        self.nodes = set()
        self.edges = []

    def add_node(self, node):
        """adds vertices to your graph"""
        if self.nodes is None:
            self.nodes = node
        else:
            self.nodes.set(node)
        return self.nodes

    def add_edge(self, last, first):
        """creates edges between two given vertices in your graph"""
        self.edges[last].append(first)
        return self.edges

    def has_edge(self, first, last):   
        """checks if a connection exists between two given nodes in your graph"""
        return self.edges[last] == first

    def remove_edge(self, last, first):
        """removes edges between two given vertices in your graph"""
        self.edges[last].pop(first)

    def remove_node(self, node):
        """removes vertices from your graph"""
        self.nodes.remove(node)
        return self.nodes

    def contains(self, node):
        """checks if your graph contains a given value"""
        if node in self.nodes:
            return True
        else:
            return False

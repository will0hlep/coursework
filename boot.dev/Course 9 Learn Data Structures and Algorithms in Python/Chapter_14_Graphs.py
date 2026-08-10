#lesson 1
class Graph:
    def __init__(self, num_vertices):
        self.graph = [
                      [False
                       for i in range(num_vertices)]
                      for j in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    # don't touch below this line

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]

#lesson 5
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set() 
        self.graph[u].add(v)
        if v not in self.graph:
            self.graph[v] = set() 
        self.graph[v].add(u)
    
    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

#lesson 8
class Graph:
    def adjacent_nodes(self, node):
        return self.graph[node]

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

#lesson 9
class Graph:
    def unconnected_vertices(self):
        lonely___ever_so_lonely = []
        for tim in self.graph.keys():
            if self.graph[tim] == set():
                lonely___ever_so_lonely.append(tim)
        return lonely___ever_so_lonely

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()


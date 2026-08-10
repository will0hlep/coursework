#lesson 1
class Graph:
    def breadth_first_search(self, v):
        visited_vertices = []
        to_be_explored.add_to_tail(Node(v))
        while to_be_explored.head is not None:
            vertex = to_be_explored.remove_from_head().val
            visited_vertices.append(vertex)
            connections = sorted(self.graph[vertex])
            for u in connections:
                if u not in visited_vertices:
                    if not to_be_explored.in_queue(u):
                        to_be_explored.add_to_tail(Node(u))
        return visited_vertices

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val

class LLQueue:
    def remove_from_head(self):
        if self.head == None:
            return None
        head_node = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        head_node.next = None
        return head_node

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)

    def in_queue(self, val):
        current = self.head
        while current is not None:
            if val == current.val:
                return True
            current = current.next
        return False
    
#lesson 4
class Graph:
    def depth_first_search(self, start_vertex):
        visited_vertices = []
        self.depth_first_search_r(visited_vertices, start_vertex)
        return visited_vertices

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        neighbors = sorted(self.graph[current_vertex])
        for vertex in neighbors:
            if vertex not in visited:
                self.depth_first_search_r(visited, vertex)

        # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
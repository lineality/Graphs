# Understand Problem and Solution
# problem: you know each single linkage of parent to child,
# but you do not know how far it is from each 'root'
# to each tree-terminal-grand-child

# approach 1:
# step 1: figure out the roots
# step 2: try each root searching for the goal-child and record the distance
# step 3: compare lengths and pick the root with
# longest rout (or the lowest number in a tie)


# Note: This Queue class is sub-optimal. Why?
class Queue:
    def __init__(self):
        self.queue = []  # note: change datastruct in future for scale

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []  #

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:

    """Representize a graph as a dictionary of
        vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # This is our adjacency list
        self.cache = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                if path[-1] == destination_vertex:
                    # print("trigger")
                    return path

                # print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
        pass  # TODO


def get_vertices_from_tuples(tuples_list):

    set_of_vertices = set()

    for this_tuple in tuples_list:
        for this_number in this_tuple:
            set_of_vertices.add(this_number)

    # sort set
    set_of_vertices = sorted(set_of_vertices)

    return set_of_vertices


def find_roots(tuples_list):
    # compare total set of items, to set of children
    # difference will be roots (no children)
    child_list = set()
    all_list = set()

    # make set of just children
    for this_tuple in tuples_list:
        # just looking at second number
        child_list.add(this_tuple[1])

    # make set of all items
    for this_tuple in tuples_list:
        # just looking at both numbers
        for this_number in this_tuple:
            all_list.add(this_number)

    # find roots (all_list - child_list)
    roots = all_list - child_list

    # return roots
    return roots


def earliest_ancestor(ancestors, starting_node):

    # step 1: make the graph

    # instantiate a graph class
    graph = Graph()

    # get list of vertices
    vertex_list = get_vertices_from_tuples(ancestors)

    for vertex in vertex_list:
        graph.add_vertex(vertex)

    # relationships: add edges
    for this_tuple in ancestors:
        # make masks
        first_item = this_tuple[0]
        second_item = this_tuple[1]

        # create (inverted) edge
        graph.add_edge(first_item, second_item)

    # Step 2: do a search
    # starting with each root
    # do a search for the target
    # and note how many step there were
    roots = find_roots(ancestors)

    pathways_list = []
    pathways_list_new = []

    for this_root in roots:
        pathways_list.append(graph.bfs(this_root, starting_node))

    # filter out None
    for item in pathways_list:
        if item:
            pathways_list_new.append(item)

    # sort order, smallest first
    pathways_list_new.sort()

    # # testing inspection
    # print("starting_node", starting_node)
    # print(pathways_list)
    # print(max(pathways_list_new, key=len))

    longest_rout = max(pathways_list_new, key=len)

    # answers:
    # check if root:
    if starting_node in roots:
        answer = -1
    else:
        # the first link in the family chain: longest ancester
        answer = longest_rout[0]

    return answer


# ancestors_tuples_list = [(1, 3), (2, 3), (3, 6), (5, 6),
#                          (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# # graph = Graph()  # Instantiate your graph
# # graph.add_vertex(1)
# # graph.add_edge(5, 3)
# starting_node = 11
# earliest_ancestor(ancestors_tuples_list, starting_node)
# print("roots", find_roots(ancestors_tuples_list))

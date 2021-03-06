"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Representize a graph as a dictionary of
        vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # This is our adjacency list

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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
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
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
        pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        ss = Stack()
        ss.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while ss.size() > 0:
            # dequeue/pop the first vertex
            path = ss.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)
        pass  # TODO

    def dft_recursive(self, vertex, path_list=None):

        # cache if path is None, instantiate empty list for traversal path
        if path_list is None:
            # create and add vertex to path-list
            path_list = [vertex]

        # readable 'mask'
        neighbor = list(self.get_neighbors(vertex))[-1]

        # check if there are any neighbors (look for base-case)
        if neighbor is not None and neighbor not in path_list:

            # if neighbor not in path_list, add it
            path_list.append(neighbor)
            # the recursvive call
            self.dft_recursive(neighbor, path_list)

        else:  # base case! no more neighbors, you done.
            print_string = ""
            # return print("end", path_list) #
            for i in path_list:
                print_string += f"{i}\n"
            print_string = print_string[:-1]
            # return print(path_list)
            return print(print_string)

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

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a q and enqueue starting vertex
        ss = Stack()
        ss.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while ss.size() > 0:
            # dequeue/pop the first vertex
            path = ss.pop()
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
                    ss.push(new_path)
        pass  # TODO

    def dfs_recursive_classroom(
        self, starting_vertex, destination_vertex, visited=None, path=None
    ):
        # edges
        edges = self.get_neighbors(starting_vertex)

        if visited is None:
            # instantiate empty set for visited
            visited = set()

        if path is None:
            # instantiate empty list for path
            path = []

        # mark current vertex as visited
        visited.add(starting_vertex)

        # defining path
        path = path + [starting_vertex]

        # when destination found, return path
        if starting_vertex == destination_vertex:
            return path

        # our base case is if we found the destination vertex,
        # so it will recurse and will define the new_path
        for edge in edges:
            if edge not in visited:
                new_path = self.dfs_recursive_classroom(
                    edge, destination_vertex, visited, path
                )
                if new_path:
                    return new_path

        # return None if path does not exist
        return None

    def dfs_recursive(self, vertex, destination_vertex, path_list=None):
        # def dft_recursive(self, vertex, path_list = None):

        # cache
        # if path is None, instantiate empty list for traversal path
        if path_list is None:
            # create and add vertex to path-list
            path_list = [vertex]

        # readable 'mask'
        neighbor = list(self.get_neighbors(vertex))[-1]
        # print("vertex", vertex)
        # print("neighbor", neighbor)
        # print("path_list", path_list)

        if neighbor is destination_vertex:
            # base case! next nightbor your check matches search
            # add it
            path_list.append(neighbor)

            return path_list

        # check if there are any neighbors (look for base-case)

        elif neighbor is not destination_vertex:
            # if neighbor not in path_list, add it
            path_list.append(neighbor)

            # the recursvive call
            return self.dfs_recursive(neighbor, destination_vertex, path_list)


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

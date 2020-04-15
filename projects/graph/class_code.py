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
                return path
            # mark as visited
            visited.add(path[-1])
            # enqueue all neightbors
            for next_vert in self.get_neighbors(path[-1]):
                new_path = list(path)
                new_path.append(next_vert)
                qq.enqueue(new_path)


def dfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    # Create a stack
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
                return path
            # mark as visited
            visited.add(path[-1])
            # enqueue all neightbors
            for next_vert in self.get_neighbors(path[-1]):
                new_path = list(path)
                new_path.append(next_vert)
                ss.push(new_path)

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

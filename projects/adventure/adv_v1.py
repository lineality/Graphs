from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
player = Player(world.starting_room)


#################################
# GGA map-graph creation code


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
        self.raw_data = {}

    # done
    def add_dungeon_vertex(self, map_file):
        """
        Add a vertex to the graph.
        """
        for room_number in range(0, len(map_file)):
            self.vertices[room_number] = set()

    # we need a sequence of rooms...
    # we also need a sequence of directions

    # can to translate a sequence of rooms into a sequence of directions
    # e.g. look up starting room in dictionary:
    # try all nsew to get direction of next room
    # record that direction...
    # maybe?

    def add_dungeon_edges(self, map_file):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # problem: we know the room connections but
        # the format is not the same as graph data
        # solution: 
        # data format: key (you want this)
        # value: list[(tuple), {dict dirction: room}]
        # the only thing we want is the room...

        # iterate through the dictionary:
        # maybe iterate through by sequential room number?
        # this give a sequential list of keys automatically: 
        # 1. get the value from the main key (which is a list)
        # 2. get the 2nd item in the list (which is a dictionary)
        # 3. iterate through the values(only) in that dictionary
        # and record those room-numbers in a linked_room_list
        # 4. iterate through linked_room_list and make tuples of the 
        # original_key and each item in the linked_room_list

        # iterate through all rooms data columns in map file
        # these should correspond to the keys
        for room_iterator in range(0, len(map_file)):
            # get room (i?)
            room_list = map_file[room_iterator]
            room_dictionary = room_list[-1]

            linked_room_list = []

            # iterate through
            for linked_room in room_dictionary.values():
                linked_room_list.append(linked_room)

            #make tuples or rooms
            for room in linked_room_list:
                # if need room tuple
                # room_tuple = (room_iterator, room)
                v1 = room_iterator
                v2 = room
                if v1 in self.vertices and v2 in self.vertices:
                    # Add the edge
                    self.vertices[v1].add(v2)
                else: 
                    print("ERROR ADDING EDGE: Vertex not found", v1, v2)


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

# test print material
#
# map_file = {
#   0: [(3, 5), {'n': 1}],
#   1: [(3, 6), {'s': 0, 'n': 2}],
#   2: [(3, 7), {'s': 1}]
# }

# dd = Graph()
# dd.add_dungeon_vertex(map_file)
# print(dd.vertices)
# dd.add_dungeon_edges(map_file)
# print(dd.vertices)

#################################


# Fill this out with directions to walk
traversal_path = ['n', 'n']
# traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

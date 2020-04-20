
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

    def bft_original(self, starting_vertex):
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


    def bft_all_path(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])

        # Create a set of traversed vertices
        visited = []

        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                
                # test print
                # print(path[-1])
                # mark as visited
                visited.extend([path[-1]])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
        return visited


    def dft_all_path(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        ss = Stack()
        ss.push([starting_vertex])
        # Create a set of traversed vertices
        visited = []
        # While queue is not empty:
        while ss.size() > 0:
            # dequeue/pop the first vertex
            path = ss.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                # print(path[-1])
                # mark as visited
                visited.extend([path[-1]])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)
        return visited



    def dfs_all_path(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a q and enqueue starting vertex
        ss = Stack()
        ss.push([starting_vertex])
        # Create a set of traversed vertices
        visited = []
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
                visited.extend([path[-1]])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)
        return visited


    def bfs_all_path(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = []
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
                visited.extend([path[-1]])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
        return visited  # TODO


# e.g. traversal_path = direction_translator()
def direction_translator(path_list):
    # translate room sequence into directions list, 
    # format: traversal_path = ['n', 'n']

    traversal_path = []
    last_room = 0
    # iterate through room squence list:
    for room in path_list:

        # printing inspection
        #print("last room is: ", last_room)
        #print("this room is: ", room)

        # skip the first time around
        if room == 0:
            pass

        # after the first time
        else:
            
            # e.g. look up last room room in dictionary:
            raw_map_data = map_file[last_room][-1]
            #print(f"raw_map_data for room ({last_room}), is: ",raw_map_data)
              
            # try all nsew to get direction of next room
            # this is looking up key by value (backwards)
            # lookup = list(raw_map_data.keys())[list(raw_map_data.values()).index(room)]
            # print("lookup", lookup)
            if 'n' in raw_map_data:
                if raw_map_data['n'] == room:
                    #print("it's north!!")
                    traversal_path.extend('n')

            if 's' in raw_map_data:
                if raw_map_data['s'] == room:
                    #print("it's south!!")
                    traversal_path.extend('s')

            if 'e' in raw_map_data:
                if raw_map_data['e'] == room:
                    #print("it's east!!")
                    traversal_path.extend('e')

            if 'w' in raw_map_data:
                if raw_map_data['w'] == room:
                    #print("it's west!!")
                    traversal_path.extend('w')

        # update last_room
        last_room = room
    
    return traversal_path


# # test line
# map_file = {
#   0: [(3, 5), {'n': 1}],
#   1: [(3, 6), {'s': 0, 'n': 2}],
#   2: [(3, 7), {'s': 1}]
# }

# test loop fork
map_file = {
  0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
  1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}],
  2: [(3, 7), {'s': 1}],
  3: [(4, 5), {'w': 0, 'e': 4}],
  4: [(5, 5), {'w': 3}],
  5: [(3, 4), {'n': 0, 's': 6}],
  6: [(3, 3), {'n': 5, 'w': 11}],
  7: [(2, 5), {'w': 8, 'e': 0}],
  8: [(1, 5), {'e': 7}],
  9: [(1, 4), {'n': 8, 's': 10}],
  10: [(1, 3), {'n': 9, 'e': 11}],
  11: [(2, 3), {'w': 10, 'e': 6}],
  12: [(4, 6), {'w': 1, 'e': 13}],
  13: [(5, 6), {'w': 12, 'n': 14}],
  14: [(5, 7), {'s': 13}],
  15: [(2, 6), {'e': 1, 'w': 16}],
  16: [(1, 6), {'n': 17, 'e': 15}],
  17: [(1, 7), {'s': 16}]
}

# # test cross
# map_file = {
#   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
#   1: [(3, 6), {'s': 0, 'n': 2}],
#   2: [(3, 7), {'s': 1}],
#   3: [(4, 5), {'w': 0, 'e': 4}],
#   4: [(5, 5), {'w': 3}],
#   5: [(3, 4), {'n': 0, 's': 6}],
#   6: [(3, 3), {'n': 5}],
#   7: [(2, 5), {'w': 8, 'e': 0}],
#   8: [(1, 5), {'e': 7}]
# }

# # test loop
# map_file = {
#   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
#   1: [(3, 6), {'s': 0, 'n': 2}],
#   2: [(3, 7), {'s': 1}],
#   3: [(4, 5), {'w': 0, 'e': 4}],
#   4: [(5, 5), {'w': 3}],
#   5: [(3, 4), {'n': 0, 's': 6}],
#   6: [(3, 3), {'n': 5, 'w': 11}],
#   7: [(2, 5), {'w': 8, 'e': 0}],
#   8: [(1, 5), {'e': 7, 's': 9}],
#   9: [(1, 4), {'n': 8, 's': 10}],
#   10: [(1, 3), {'n': 9, 'e': 11}],
#   11: [(2, 3), {'w': 10, 'e': 6}]
# }



# instantiation of graph class
dd = Graph()

# entering rooms as nodes/vertices
dd.add_dungeon_vertex(map_file)
# checking that rooms were entered
# print(dd.vertices)

# add edges
dd.add_dungeon_edges(map_file)
# checking that edges were entered
print("edges", dd.vertices)




# idea: combine and reduce length of paths
# 
# comparing a BFS for every room...
# graph comparison...
# duplicate the shortest paths...

# some paths are going to be a complete subset of others...
# e.g. bfs 0,1 bfs 0,2
# rule 1: if 2 paths overlap, remove the shorter one (done)

# rule 2: if 2 paths partially overlap, but partially not, 
# then delete the part that does overlap from all but one list.

# rule 3: if 2 path don't overlap at all, reverse-duplicate the shorter.

# Step: look to see what sets are completely included in other sets
# >>> t.issubset(s)
# True
# >>> s.issuperset(t)
# True

list_of_rout_lists = []

for i in range(1, len(map_file)):
    list_of_rout_lists.extend([dd.dfs_all_path(0,i)])

print("list_of_rout_lists", list_of_rout_lists)


def remove_subset_paths(list_of_rout_lists):


    list_of_rout_lists = []

    for i in range(1, len(map_file)):
        list_of_rout_lists.extend([dd.dfs_all_path(0,i)])

    # printing, inspection
    print("list_of_rout_lists", list_of_rout_lists)

    changes_made_flag = True

    # keep going while changes are being made
    while changes_made_flag == True:
        changes_made_flag = False

        # compare all items
        for list1 in list_of_rout_lists:
            for list2 in list_of_rout_lists:
                set_list1 = set(list1)
                set_list2 = set(list2)
                if list1 != list2:
                    # remove whatever is a subset
                    if list1 in list_of_rout_lists:
                        if set_list1.issubset(set_list2):
                            # inspection
                            # print("yes")
                            # print(list_of_rout_lists)
                            # print("1 is sub", list1)
                            # print("2", list2)
                            list_of_rout_lists.remove(list1)
                            # update flag
                            changes_made_flag = True

    return list_of_rout_lists

list_of_rout_lists = []
list_of_rout_lists = remove_subset_paths(list_of_rout_lists)
print("this has no sub-set duplications" )
print(list_of_rout_lists)


# Step 2: remove all but one copy of overlapping portions:
# remove all but the one (last) shared part 
# from all but one sub-list

def remove_partial_overlap(list_of_rout_lists):

    # create changes flag
    changes_made_flag = True

    # keep going while changes are being made
    while changes_made_flag == True:
        changes_made_flag = False

        # compare all items
        for list1 in list_of_rout_lists:
            for list2 in list_of_rout_lists:

                if list1 != list2:
                    # get the shared path
                    shared_path = set(list1) & set(list2)
                    # let one shared node remain
                    shorter_shared_path = list(shared_path)[:-1]

                    # remove whatever is a subset
                    if list1 in list_of_rout_lists:
                        # compare: if the shared path exists
                        # i.e. if it is not Length = Zero
                        if len(shorter_shared_path) > 0: 
                            # # inspection
                            # print("yes, shorter")
                            # print(list_of_rout_lists)
                            # print("1", list1)
                            # print("2", list2)
                            # remove shared items from just one
                            # of the two
                            for i in shorter_shared_path:
                                list2.remove(i)
                            # update flag
                            changes_made_flag = True

    return list_of_rout_lists

list_of_rout_lists = remove_partial_overlap(list_of_rout_lists)
print("this has no overlaps")
print(list_of_rout_lists)


# Step 3: 
# sequence the parts to match up
# maybe just sort?
list_of_rout_lists.sort()
print("this is optimally sorted (maybe")
print(list_of_rout_lists)

# Step 4:
# stitch together the paths

def path_frankenstein(list_of_rout_lists):

    # attach the second path to the first, 
    # by addding between the two
    # the a shortest path 
    # from that last location in path 1
    # to first location in path 2
    # then add that new glue path
    # to the end of the first path
    # Do this for each item and the next
    # lastly 
    # concatonate all these lists into one big path

    while len(list_of_rout_lists) > 1:
        # get the two paths
        path1 = list_of_rout_lists[0]
        path2 = list_of_rout_lists[1]

        # get the to-match-up ends of the paths
        last_room_in_path1 = path1[-1]
        first_room_in_path2 = path2[0]

        # get the glue path to match them up
        new_glue_path = dd.bfs_all_path(last_room_in_path1,first_room_in_path2)

        # add the glue path to the first path
        # (& remove the overlapping room!)
        path1.pop()
        path1.extend(new_glue_path)

        # add list2 to list1 (& remove the overlapping room!)
        path2.pop(0)
        path1.extend(path2)
        # delete path 2 from the list
        list_of_rout_lists.pop(1)

    list_of_rout_lists = list_of_rout_lists[0]

    # return the new list of paths
    return list_of_rout_lists

traversal_path = path_frankenstein(list_of_rout_lists)
print("a list of directions by room")
print(traversal_path)
print(len(traversal_path))
# Step 5:
# convert to directions (N,S,E,W)

# translate the room-path into a direction-walking path
traversal_path = direction_translator(traversal_path)

# checking trav path output
print(len(traversal_path))
print(traversal_path)
